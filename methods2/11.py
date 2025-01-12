import numpy as np
import math

def f1(x):
    return x**2 - 3 + 0.5**x

def f2(x):
    return 3*x**4 - 8*x**3 - 18*x**2 + 2

def f3(x):
    return math.atan(x)-1/(3*x**3)


def bisection(f, a, b, tol):
    c = a
    while ((b-a) >= tol):
        c = (a+b)/2
        if (f(c) == 0):
            break
        if (f(c)*f(a) < 0):
            b = c
        else:
            a = c
    return c

a = 100
t = -100
b = 2
k = 0
m = 0.1
l = 1
tol = 0.01


x1 = bisection(f1, a, b, tol)
x2 = bisection(f2, k, l, tol)
x3 = bisection(f3, m, a, tol)



print("Корень уравнения f3: ", x3)

x3 = bisection(f3, t,m , tol)
print("Корень уравнения f3: ", x3)
# Оценка погрешности

err3 = abs(1-abs(10*tol-(x3 - np.sqrt(3)/10)))

print("Погрешность для f3: ", err3)