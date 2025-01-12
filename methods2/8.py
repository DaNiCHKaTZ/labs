import numpy as np
import matplotlib.pyplot as plt



def f(x, y):
    return 1 + (1 - x) * np.sin(y) - (2 + x) * y


def u_exact(x):
    return np.sin(x) + np.exp(-np.sin(x)) - 1


u0 = 0
x0 = 0
X = 2


h = 0.01


x = np.arange(x0, X, h)
u = np.zeros_like(x)
u[0] = u0


for i in range(1, len(x)):
    u[i] = u[i-1] + h * f(x[i-1], u[i-1])


u_euler_koshi = np.zeros_like(x)
u_euler_koshi[0] = u0

for i in range(1, len(x)):
    f1 = f(x[i-1], u_euler_koshi[i-1])
    u_temp = u_euler_koshi[i-1] + h * f1
    f2 = f(x[i], u_temp)
    u_euler_koshi[i] = u_euler_koshi[i-1] + h * (f1 + f2) / 2

u_runge_kutta = np.zeros_like(x)
u_runge_kutta[0] = u0

for i in range(1, len(x)):
    k1 = h * f(x[i-1], u_runge_kutta[i-1])
    k2 = h * f(x[i-1] + h/2, u_runge_kutta[i-1] + k1/2)
    k3 = h * f(x[i-1] + h/2, u_runge_kutta[i-1] + k2/2)
    k4 = h * f(x[i-1] + h, u_runge_kutta[i-1] + k3)
    u_runge_kutta[i] = u_runge_kutta[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6


plt.figure(figsize=(10, 8))
plt.plot(x, u, label='Метод Эйлера')
plt.plot(x, u_euler_koshi, label='Метод Эйлера-Коши')
plt.plot(x, u_runge_kutta, label='Метод Рунге-Кутты')
plt.plot(x, u_exact(x), label='Точное решение')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Сравнение решений дифференциального уравнения')
plt.legend()
plt.show()
u_exact_values = u_exact(x)


error_euler = np.abs(u - u_exact_values)
error_euler_koshi = np.abs(u_euler_koshi - u_exact_values)
error_runge_kutta = np.abs(u_runge_kutta - u_exact_values)


max_error_euler = np.max(error_euler)
max_error_euler_koshi = np.max(error_euler_koshi)
max_error_runge_kutta = np.max(error_runge_kutta)

print(f"Максимальная абсолютная погрешность для метода Эйлера: {max_error_euler}")
print(f"Максимальная абсолютная погрешность для метода Эйлера-Коши: {max_error_euler_koshi}")
print(f"Максимальная абсолютная погрешность для метода Рунге-Кутты: {max_error_runge_kutta}")