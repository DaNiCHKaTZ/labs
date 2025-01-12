import numpy as np
import matplotlib.pyplot as plt


x_points = np.array([2.70, 2.75, 2.80, 2.85, 2.90, 2.95, 3.00, 3.05])
y_points = np.array([1.5297, 1.4865, 1.4435, 1.4030, 1.3658, 0.9071, 0.8709, 0.8437])

def lagrange(x, x_points, y_points):
    total = 0
    n = len(x_points)
    for i in range(n):
        xi, yi = x_points[i], y_points[i]
        def g(i, n): 
            tot_mul = 1
            for j in range(n):
                if i != j:
                    xj = x_points[j]
                    tot_mul *= (x - xj) / float(xi - xj)
            return tot_mul

        total += yi * g(i, n)
    return total


def newton(x, x_points, y_points):55
    n = len(x_points)
    a = np.zeros(n)
    for i in range(n):
        a[i] = y_points[i]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x_points[i]-x_points[i-j])
    p = a[n-1]
    for i in range(n-2, -1, -1):
        p = a[i] + (x - x_points[i])*p
    return p


x_eval = np.linspace(x_points[0], x_points[-1], num=1000)


y_lagrange = [lagrange(x, x_points, y_points) for x in x_eval]
y_newton = [newton(x, x_points, y_points) for x in x_eval]

error_lagrange = np.abs(y_points - np.array([lagrange(x, x_points, y_points) for x in x_points]))
error_newton = np.abs(y_points - np.array([newton(x, x_points, y_points) for x in x_points]))


plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_eval, y_lagrange, label='Лагранж')
plt.plot(x_eval, y_newton, label='Ньютон')
plt.scatter(x_points, y_points, color='red')
plt.title('Интерполяционные многочлены')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()



plt.tight_layout()
plt.show()