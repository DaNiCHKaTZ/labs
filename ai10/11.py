import numpy as np
import matplotlib.pyplot as plt
from keras.src import Sequential
from keras.src.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.src.utils import to_categorical
from sklearn.model_selection import train_test_split
from skimage import draw

shape_types ={0 : 'square', 1 : 'triangle', 2 : 'circle'}

def generate_shapes(num_samples):
    data = []
    labels = []
    for _ in range(num_samples):
        shape_type = np.random.choice(['square', 'triangle', 'circle'])
        label = {'square': 0, 'triangle': 1, 'circle': 2}[shape_type]
        labels.append(label)
        
        img = np.zeros((64, 64))
        
        if shape_type == 'square':
            x, y = np.random.randint(5, 50, size=2)
            size = np.random.randint(5, 15)
            img[x:x+size, y:y+size] = 1
        elif shape_type == 'triangle':
            x = np.random.randint(5, 50, size=3)
            y = np.random.randint(5, 50, size=3)
            rr, cc = draw.polygon_perimeter(x, y)
            img[rr, cc] = 1
        elif shape_type == 'circle':
            r = np.random.randint(4, 10)
            x, y = np.random.randint(5, 45, size=2)
            rr, cc, val = draw.circle_perimeter_aa(x, y, r)
            img[rr, cc] = 1
        
        data.append(img)
    
    data = np.array(data)
    data = data.reshape(num_samples, 64, 64, 1)
    labels = to_categorical(np.array(labels), 3)
    
    return data, labels




data, labels = generate_shapes(1000)
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)


model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10)


loss, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy * 100:.2f}%')


def plot_example(index):
    plt.imshow(X_test[index].reshape(64, 64), cmap='gray')
    plt.title(f'Prediction: {shape_types[np.argmax(model.predict(X_test[index].reshape(1, 64, 64, 1)))]}')
    plt.show()

plot_example(0) 