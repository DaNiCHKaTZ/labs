import numpy as np

def equations(vars):
    x, y = vars
    eq1 = np.sin(x) - y + 1.32
    eq2 = np.cos(y) - x + 0.85
    return np.array([eq1, eq2])

def jacobian(vars):
    x, y = vars
    j = np.array([[np.cos(x), -1], [0, -np.sin(y)]])
    return j

def newton_method(x0, y0, e, max_iter=100):
    x, y = x0, y0
    iterations = 0
    while iterations < max_iter:
        iterations += 1
        f = equations((x, y))
        j = jacobian((x, y))
        delta = np.linalg.solve(j, f)
        x_new = x - delta[0]
        y_new = y - delta[1]
        error = max(abs(x_new - x), abs(y_new - y))
        if error < e:
            return x_new, y_new, iterations, error
        x, y = x_new, y_new
    return None, None, iterations, error

x0, y0 = -0.3, 0.2  
e = 0.001  
x, y, iterations, error = newton_method(x0, y0, e)

if x is None:
    print("Метод Ньютона не сходится")
else:
    print(f'Решение: x = {x}, y = {y}')
    print(f'Число итераций: {iterations}')
    print(f'Погрешность решения: {error}')