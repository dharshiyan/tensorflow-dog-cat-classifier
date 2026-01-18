#import
import cv2
import numpy as np
from tensorflow import keras
model = keras.models.load_model("dog_cat_classifier.keras")

#test
img = cv2.imread("dog.jpg") #add image
img = cv2.resize(img, (128,128))
img = img / 255.0
img = np.expand_dims(img, axis=0)

prediction = model.predict(img)

#result
if prediction[0] > 0.5:
    print("🐶 Dog")
else:
    print("🐱 Cat")
