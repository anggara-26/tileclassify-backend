# Tile Classification API

## Overview

This project provides a backend API for a roof tile classification system. It uses a trained machine learning model to identify different types of roof tiles from images and categorizes their price ranges. The API is built with Django and Django REST Framework, supporting a mobile application that enables users to upload pictures of roof tiles for classification. I don't push the pre-trained model, so you can use or modify it with your own omdel.

## Features

- Image upload endpoint for tile classification
- AI-based classification of 8 types of roof tiles:
  - Asbes (Asbestos)
  - Aspal (Asphalt)
  - Beton (Concrete)
  - Jerami (Straw)
  - Keramik (Ceramic)
  - Seng (Zinc)
  - Spandek (Metal sheet)
  - Tanah Liat (Clay)
- Price category classification (murah/sedang/mahal - cheap/medium/expensive)
- Confidence score for each prediction
- Health check endpoint

## Technology Stack

- **Backend Framework**: Django, Django REST Framework
- **AI/ML**: TensorFlow, Keras
- **Database**: SQLite (development)
- **Language**: Python

## Project Structure

```
bantu_dosen/
├── api/                  # API application
│   ├── ai/               # AI model implementation
│   │   ├── weights/      # Pre-trained model files
│   │   └── tile.py       # Tile classifier implementation
│   ├── migrations/       # Database migrations
│   ├── models.py         # Database models
│   ├── serializers.py    # API serializers
│   ├── urls.py           # API endpoints
│   └── views.py          # API views
├── media/                # Media storage
│   └── images/           # Uploaded images
├── tile/                 # Project settings
└── manage.py             # Django management script
```

## API Endpoints

- `GET /health-check/` - Check if the API is running
- `POST /api/classify-tile/` - Upload an image for tile classification

## Setup and Installation

### Prerequisites

- Python 3.10+
- pip
- virtualenv (optional)

### Installation Steps

1. Clone the repository

   ```bash
   git clone https://github.com/anggara-26/tileclassify-backend.git
   cd tileclassify-backend
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations

   ```bash
   python manage.py migrate
   ```

5. Run the development server
   ```bash
   python manage.py runserver
   ```

## Usage

To classify a tile image, send a POST request to `/api/classify-tile/` with an image file. Example using curl:

```bash
curl -X POST \
  http://127.0.0.1:8000/api/classify-tile/ \
  -F "image_file=@/path/to/your/image.jpg" \
  -F "confidence_threshold=0.5"
```

The API will return a JSON response with the classification result:

```json
{
  "message": "Tile classification successful",
  "data": {
    "tile_type": "keramik",
    "tile_price": "mahal",
    "confidence": "95.78%"
  },
  "status": 200
}
```

## Contributing

This project was created to assist my university lecturers with their research on roof tile classification. If you'd like to contribute, please contact the repository owner.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the university lecturers who provided the AI model and research guidance
