#!/bin/bash
set -e

echo "=== Django Application Startup ==="

# Check if manage.py exists
if [ ! -f "manage.py" ]; then
    echo "ERROR: manage.py not found in $(pwd)"
    ls -la
    exit 1
fi

# Check Python and Django
echo "Python version: $(python --version)"
echo "Current directory: $(pwd)"
echo "Django check..."
python manage.py check --deploy

# Wait for database
echo "Waiting for database..."
until python -c "
import os
import psycopg2
try:
    psycopg2.connect(
        host=os.environ.get('DATABASE_HOST', 'db'),
        port=os.environ.get('DATABASE_PORT', '5432'),
        user=os.environ.get('DATABASE_USER', 'dbuser'),
        password=os.environ.get('DATABASE_PASSWORD', ''),
        database=os.environ.get('DATABASE_NAME', 'dockerdjango')
    )
    print('Database is ready!')
except Exception as e:
    print(f'Database not ready: {e}')
    exit(1)
"; do
  echo "Waiting for database..."
  sleep 2
done

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Start Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 60 tile.wsgi:application