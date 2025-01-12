import numpy as np

sales = np.array([80, 79, 85, 80, 75, 68, 65, 68, 65, 62])

sales = (sales - np.min(sales)) / (np.max(sales) - np.min(sales))

X = []
y = []
kol = 3

for i in range(len(sales) - kol):
    X.append(sales[i:i + kol])
    y.append(sales[i + kol])

X = np.array(X)
y = np.array(y).reshape(-1, 1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))
        self.weights1 += d_weights1
        self.weights2 += d_weights2


nn = NeuralNetwork(X, y)

for _ in range(10000):  
    nn.feedforward()
    nn.backprop()


def predict(nn, data):
    layer1 = sigmoid(np.dot(data, nn.weights1))
    output = sigmoid(np.dot(layer1, nn.weights2))
    return output

last_window = sales[-kol:]
predicted_value = predict(nn, last_window.reshape(1, -1))

predicted_value = predicted_value * (np.max(sales) - np.min(sales)) + np.min(sales)

print(f"Прогнозируемый объем продаж: {predicted_value[0][0]:.2f} миллиона рублей")
