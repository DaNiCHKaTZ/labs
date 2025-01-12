import cv2
import pytesseract
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import scipy.io
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img

def load_emnist_data():
    path = 'matlab/emnist-letters.mat'
    if not os.path.exists(path):
        raise FileNotFoundError("Not found.")
    
    data = scipy.io.loadmat(path)
    
    X_train = data['dataset'][0][0]['train'][0][0]['images'].reshape(-1, 28, 28, 1)
    y_train = data['dataset'][0][0]['train'][0][0]['labels']
    X_test = data['dataset'][0][0]['test'][0][0]['images'].reshape(-1, 28, 28, 1)
    y_test = data['dataset'][0][0]['test'][0][0]['labels']
    
    X_train = X_train / 255.0
    X_test = X_test / 255.0
    
    y_train = y_train - 1
    y_test = y_test - 1
    
    y_train = to_categorical(y_train, num_classes=26)
    y_test = to_categorical(y_test, num_classes=26)
    
    return (X_train, y_train), (X_test, y_test)

(X_train, y_train), (X_val, y_val) = load_emnist_data()

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(26, activation='softmax')  
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

def recognize_letters(image_path):
    img = preprocess_image(image_path)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    letters = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        letter_img = img[y:y+h, x:x+w]
        letter_img = cv2.resize(letter_img, (28, 28))
        letter_img = letter_img.reshape(1, 28, 28, 1) / 255.0
        prediction = model.predict(letter_img)
        predicted_letter = chr(np.argmax(prediction) + ord('A'))
        letters.append((x, predicted_letter))
    
    letters.sort(key=lambda x: x[0])
    
    predicted_word = ''.join([letter[1] for letter in letters])
    return predicted_word

image_path = 'test.png'
processed_image = preprocess_image(image_path)

predicted_word = recognize_letters(image_path)
print("Предсказанное слово:", predicted_word)

with open("predicted_word.txt", "w", encoding="utf-8") as file:
    file.write(predicted_word)
