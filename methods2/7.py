import numpy as np

def f(x):
    return x/((np.sin(3*x)**2))

a, b = 0.2, 1
exact_integral = 2.2818 

n = 1000
h = (b - a) / n

def rectangle_method(a, b, n):
    h = (b - a) / n
    result = sum([f(a + i * h) for i in range(n)]) * h
    return result

def trapezoidal_method(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b)) + sum([f(a + i * h) for i in range(1, n)])
    result *= h
    return result

def simpson_method(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = h / 3 * (y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2]))
    return result

rectangle_sum = rectangle_method(a, b, n)
trapezoidal_sum = trapezoidal_method(a, b, n)
simpson_sum = simpson_method(a, b, n)

print("Точный ответ: ", exact_integral)
print("Метод прямоугольников:", rectangle_sum)
print("Метод трапеций:", trapezoidal_sum)
print("Метод Симпсона:", simpson_sum)


rectangle_error = abs(rectangle_sum - exact_integral)
trapezoidal_error = abs(trapezoidal_sum - exact_integral)
simpson_error = abs(simpson_sum - exact_integral)
print("\nПогрешности:")
print("Метод прямоугольников:", rectangle_error)
print("Метод трапеций:", trapezoidal_error)
print("Метод Симпсона:", simpson_error)

def find_n_for_accuracy(method, exact_value, a, b, accuracy=1e-3):
    n = 1
    while True:
        approx = method(a, b, n)
        error = abs(approx - exact_value)
        if error < accuracy:
            return n
        n *= 2

n_rectangle = find_n_for_accuracy(rectangle_method, exact_integral, a, b)
n_trapezoidal = find_n_for_accuracy(trapezoidal_method, exact_integral, a, b)
n_simpson = find_n_for_accuracy(simpson_method, exact_integral, a, b)

print("\nКоличество разбиений для достижения 3 верных цифр:")
print("Метод прямоугольников:", n_rectangle)
print("Метод трапеций:", n_trapezoidal)
print("Метод Симпсона:", n_simpson)

def gauss(f, a, b, n):
    nodes, weights = np.polynomial.legendre.leggauss(n)
    integral = 0
    for i in range(n):
        x = 0.5 * (b - a) * nodes[i] + 0.5 * (a + b)
        integral += weights[i] * f(x)
    integral *= 0.5 * (b - a)
    return integral

gauss_integral = gauss(f, a, b, n)

gauss_error = abs(gauss_integral - exact_integral)
print("\nМетод Гаусса:", gauss_integral)

