import numpy as np

def equations(vars):
    x, y = vars
    eq1 = np.sin(x) - y + 1.32
    eq2 = np.cos(y) - x + 0.85
    return [eq1, eq2]

def simple_iteration(x0, y0, e):
    x, y = x0, y0
    iterations = 0
    while True:
        iterations += 1
        x_new = np.sin(y + 1) - 1.2
        y_new = (1 - np.cos(x)) / 2
        error = max(abs(x_new - x), abs(y_new - y))
        if error < e:
            break
        x, y = x_new, y_new
    return x_new, y_new, iterations, error

x0, y0 = -0.5, 0.5  
e = 0.001  
x, y, iterations, error = simple_iteration(x0, y0, e)

print(f'Решение: x = {x}, y = {y}')
print(f'Число итераций: {iterations}')
print(f'Погрешность решения: {error}')
