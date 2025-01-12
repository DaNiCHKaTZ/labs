import math

def f(x):
    return x**3+4*x-6
def f_prime(x):
    return 3*x**2+4
def newton_method(initial_guess, tolerance=0.001, max_iterations=100):
    x = initial_guess
    for iteration in range(max_iterations):
        x_next = x - f(x) / f_prime(x)
        if abs(x_next - x) < tolerance:
            break
        x = x_next
    return x, iteration


initial_guess = 0.5


root1, iterations1 = newton_method(initial_guess)
print(f"Первый корень: x1 ≈ {root1:.6f} (число итераций: {iterations1})")

