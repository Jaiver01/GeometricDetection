from tensorflow import keras
import tensorflow_hub as hub
from PIL import Image
import numpy as np
from io import BytesIO
import cv2
import os

current_directory = os.getcwd()
model = keras.models.load_model(
    current_directory + '/classifier/trained_model/geometric_classifier.h5',
    custom_objects = { 'KerasLayer': hub.KerasLayer }
)

categories = ['Círculo', 'Cuadrado', 'Hexágono', 'Rectángulo', 'Triángulo']

def classify(url):
    img = Image.open(url)

    img = np.array(img).astype(float) / 255

    img = cv2.resize(img, (224, 224))
    prediction = model.predict(img.reshape(-1, 224, 224, 3))

    return categories[np.argmax(prediction[0], axis = -1)]