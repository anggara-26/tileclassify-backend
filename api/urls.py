from django.urls import path
from .views import HealthCheckView, TileClassifierView


urlpatterns = [
    path('healthcheck/', HealthCheckView.as_view(), name='healthcheck'),
    path('classify-tile/', TileClassifierView.as_view(), name='tile_classifier'),
]