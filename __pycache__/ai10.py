import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing import image

os.makedirs('data/squares', exist_ok=True)
os.makedirs('data/triangles', exist_ok=True)
os.makedirs('data/circles', exist_ok=True)

def generate_square(canvas_size, shape_size):
    img = np.ones((canvas_size, canvas_size, 3), dtype=np.uint8) * 255
    angle = np.random.uniform(-45, 45)
    x = np.random.randint(0, canvas_size - shape_size)
    y = np.random.randint(0, canvas_size - shape_size)
    rotation_matrix = cv2.getRotationMatrix2D((x + shape_size // 2, y + shape_size // 2), angle, 1.0)
    square = np.array([[x, y], [x + shape_size, y], [x + shape_size, y + shape_size], [x, y + shape_size]], dtype=np.int32)
    cv2.polylines(img, [square], isClosed=True, color=(0, 0, 0), thickness=3)
    img = cv2.warpAffine(img, rotation_matrix, (canvas_size, canvas_size), borderValue=(255, 255, 255))
    return img

def generate_triangle(canvas_size, shape_size):
    img = np.ones((canvas_size, canvas_size, 3), dtype=np.uint8) * 255
    half_size = shape_size // 2
    x = np.random.randint(half_size, canvas_size - half_size)
    y = np.random.randint(half_size, canvas_size - half_size)
    points = np.array([[x, y - half_size], [x - half_size, y + half_size], [x + half_size, y + half_size]])
    angle = np.random.uniform(-45, 45)
    rotation_matrix = cv2.getRotationMatrix2D((x, y), angle, 1.0)
    cv2.drawContours(img, [points], 0, (0, 0, 0), 3)
    img = cv2.warpAffine(img, rotation_matrix, (canvas_size, canvas_size), borderValue=(255, 255, 255))
    return img

def generate_circle(canvas_size):
    img = np.ones((canvas_size, canvas_size, 3), dtype=np.uint8) * 255
    radius = np.random.randint(10, canvas_size // 2 - 10)
    x = np.random.randint(radius, canvas_size - radius)
    y = np.random.randint(radius, canvas_size - radius)
    cv2.circle(img, (x, y), radius, (0, 0, 0), 3)
    return img

canvas_size = 128 
shape_size = 64  

for i in range(200):
    square = generate_square(canvas_size, shape_size)
    triangle = generate_triangle(canvas_size, shape_size)
    circle = generate_circle(canvas_size)
    _, square_bin = cv2.threshold(cv2.cvtColor(square, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
    _, triangle_bin = cv2.threshold(cv2.cvtColor(triangle, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
    _, circle_bin = cv2.threshold(cv2.cvtColor(circle, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f'data/squares/square_{i}.png', square_bin)
    cv2.imwrite(f'data/triangles/triangle_{i}.png', triangle_bin)
    cv2.imwrite(f'data/circles/circle_{i}.png', circle_bin)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(canvas_size, canvas_size, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=45, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory('data', color_mode='grayscale', target_size=(canvas_size, canvas_size), batch_size=32, class_mode='categorical')
validation_generator = test_datagen.flow_from_directory('data', color_mode='grayscale', target_size=(canvas_size, canvas_size), batch_size=32, class_mode='categorical')

history = model.fit(train_generator, epochs=10, validation_data=validation_generator)

test_loss, test_acc = model.evaluate(validation_generator)
print(f'Точность на тестовых данных: {test_acc}')

img_path = input("Введите путь к вашему изображению: ")
img = image.load_img(img_path, color_mode='grayscale', target_size=(canvas_size, canvas_size))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)
prediction = model.predict(img_array)
class_idx = np.argmax(prediction[0])
classes = ['Окружность', 'Квадрат', 'Треугольник']
print(f'Предсказанная фигура: {classes[class_idx]}')
