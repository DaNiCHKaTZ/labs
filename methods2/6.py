import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import minimize

def my_curve_fit(func, xdata, ydata, learning_rate=0.01, num_iterations=1000):
    
    params = np.zeros(func.__code__.co_argcount - 1)

    for _ in range(num_iterations):
        
        error = ydata - func(xdata, *params)

       
        gradients = -2 * error.dot(np.array([func(xdata, *(params - np.eye(len(params))[i] * 1e-5)) for i in range(len(params))]).T) / 1e-5

        
        params -= learning_rate * gradients

    return params


x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
y = np.array([3.02, 2.81, 2.57, 2.39, 2.18, 1.99, 1.81 ,1.85])

plt.scatter(x, y, label='Исходные данные')


def line(x, a, b):
    return a * x + b

def quadro(x, a, b, c):
    return a * x**2 + b * x + c

def drob(x, a, b):
    return 1/(a*x+b)


funcs = [line, quadro, drob]

for func in funcs:
    params, _ = curve_fit(func, x, y)
    plt.plot(x, func(x, *params), label=f'{func.__name__} fit')

for func in funcs:
    params, _ = curve_fit(func, x, y)
    y_pred = func(x, *params)
    deviation = np.abs(y - y_pred)
    print(f'Погрешность {func.__name__}: {deviation}')

plt.legend()
plt.show()
