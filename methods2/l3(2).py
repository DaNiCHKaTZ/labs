def f(x):
    return x**3+4*x-6

def chord_method(x0, x1, epsilon=0.001, max_iterations=100):
    for iteration in range(max_iterations):
        f_x0 = f(x0)
        f_x1 = f(x1)
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        
        if abs(x2 - x1) < epsilon:
            return x2, iteration + 1
        
        x0, x1 = x1, x2
    
    return None, max_iterations

import math


x0 = 0.5
x1 = 1.5

root, iterations = chord_method(x0, x1)

if root is not None:
    print(f"Приближенный корень: x ≈ {root:.3f}")
    print(f"Число итераций: {iterations}")
else:
    print("Метод хорд не сошелся за заданное количество итераций.")
