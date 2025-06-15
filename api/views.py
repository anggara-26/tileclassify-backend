from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ImageUpload, Detections
from .ai.tile import TileClassifier
from .serializers import ImageUploadSerializer


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": 200, "message": "It's Running :D"}, status=200)

class TileClassifierView(APIView):
    detector = TileClassifier()
    serializer_class = ImageUploadSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image_upload = serializer.save()
            image_path = image_upload.image_file.path
            tile_type, tile_price, confidence = self.detector.predict_tile_and_price(image_path)

            # Simpan hasil deteksi ke database
            detection = Detections(
                object_detection=image_upload,
                label=tile_type,
                confidence=confidence,
                x_min=0.0,
                x_max=1.0,
                y_min=0.0,
                y_max=1.0
            )
            detection.save()

            return Response({
                "message": "Tile classification successful",
                "data": {
                    "tile_type": tile_type,
                    "tile_price": tile_price,
                    "confidence": f"{confidence*100:.2f}%"  # Menambahkan confidence ke response
                },
                "status": status.HTTP_200_OK,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)