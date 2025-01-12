import math

def g(x):
    return math.cos(x)

def f(x):
    return x**3 + 0.2*x**2 + 0.5*x + 0.8

def it_method(init, tol=0.001, max_it=30):
    x = init
    for i in range(max_it):
        x_next = f(x)
        if abs(x_next - x) < tol:
            return x_next, i + 1
        x = x_next
    return None, max_it

init = -0.8
root, it = it_method(init)

if root is not None:
    print(f"Уточненный корень: {root:.3f}")
    print(f"Число итераций: {it}")
else:
    print("Метод не сошелся за заданное количество итераций.")
