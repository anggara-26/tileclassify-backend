import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import os

from tile.settings import BASE_DIR

class TileClassifier:
    def __init__(self):
        # Load model dari file .h5
        model_path = os.path.join(BASE_DIR, 'api', 'ai', 'weights', 'tile_classification_model.h5')
        print(f"Loading model from: {model_path}")
        self.model = load_model(model_path)

        # Mapping label index ke nama genteng
        self.label_map = {
            0: 'asbes',
            1: 'aspal',
            2: 'beton',
            3: 'jerami',
            4: 'keramik',
            5: 'seng',
            6: 'spandek',
            7: 'tanahliat'
        }

        # Mapping harga
        self.price_map = {
            'beton': 'sedang',
            'keramik': 'mahal',
            'asbes': 'murah',
            'jerami': 'murah',
            'seng': 'murah',
            'aspal': 'sedang',
            'spandek': 'sedang',
            'tanahliat': 'mahal'
        }

    # Method untuk memprediksi jenis genteng dan kategori harga
    def predict_tile_and_price(self, image_path):
        img = image.load_img(image_path, target_size=(128, 128))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = self.model.predict(img_array)
        predicted_class_idx = np.argmax(prediction[0])
        confidence = float(prediction[0][predicted_class_idx])  # Extract the confidence value
        tile_type = self.label_map[predicted_class_idx]
        tile_price = self.price_map[tile_type]

        print(f"Jenis genteng     : {tile_type}")
        print(f"Confidence        : {confidence:.4f} ({confidence*100:.2f}%)")
        print(f"Kategori harga    : {tile_price}")
        
        return tile_type, tile_price, confidence
