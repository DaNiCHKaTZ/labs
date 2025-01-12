import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator, image
import numpy as np


model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')  
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = datagen.flow_from_directory(
    'path_to_data',
    target_size=(64, 64),
    color_mode='grayscale',
    batch_size=32,
    class_mode='sparse',
    subset='training'
)

validation_generator = datagen.flow_from_directory(
    'path_to_data',
    target_size=(64, 64),
    color_mode='grayscale',
    batch_size=32,
    class_mode='sparse',
    subset='validation'
)

model.fit(train_generator, epochs=10, validation_data=validation_generator)


loss, accuracy = model.evaluate(validation_generator)
print(f'Accuracy: {accuracy*100:.2f}%')


img = image.load_img('', target_size=(64, 64), color_mode='grayscale')
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)
predicted_class = np.argmax(prediction[0])

classes = ['Квадрат', 'Треугольник', 'Окружность']
print(f'Predicted class: {classes[predicted_class]}')
