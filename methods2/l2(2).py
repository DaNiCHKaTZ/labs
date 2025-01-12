import numpy as np

def f(x):
    return x**3 + 0.2*x**2 + 0.5*x + 0.8

def df(x):
    return 3*x**2 + 0.4*x + 0.5

def simple_iteration(x0, eps):
    x = x0
    n = 0
    while True:
        n += 1
        x_prev = x
        x = x - f(x) / df(x)
        if abs(x - x_prev) < eps:
            break
    return x, n

x0 = -0.1 
xn = -1
eps = 0.0001 
x, n = simple_iteration(x0, eps)
if (df(x)>1):
    print("Метод не сходится")
else:
    print(f"Корень уравнения: {x}")
    print(f"Число итераций: {n}")
    print(f"Погрешность: {0.808+x}")
    