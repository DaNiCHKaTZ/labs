import numpy as np
import matplotlib.pyplot as plt

f = lambda x: -1/x
a, b, h = 1, 10, 2
x_interp = np.array([2.24, 4.63, 7.944])

x = np.arange(a, b+h, h)
y = f(x)

def divided_diff(x, y):
    n = len(y)
    N = np.zeros([n, n])
    N[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
           N[i][j] = (N[i+1][j-1] - N[i][j-1]) / (x[i+j]-x[i])
            
    return N

def newton_poly(coef, x_data, x):
    n = len(x_data) - 1 
    p = N[n]
    for k in range(1,n+1):
        p = N[n-k] + (x -x_data[n-k])*p
    return p

coef = divided_diff(x, y)[0, :]

y_interp = newton_poly(coef, x, x_interp)
print(f'Значения интерполяции в точках {x_interp}: {y_interp}')  # добавленная строка
errors = np.abs(y_interp - f(x_interp))
for i, error in enumerate(errors):
    print(f'Погрешность интерполяции в точке {x_interp[i]}: {error}')
    
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='f(x)')
plt.plot(x_interp, y_interp, 's', label='Точки интерполяции')
plt.plot(np.linspace(a, b, 1000), newton_poly(coef, x, np.linspace(a, b, 1000)), label='Интерполяционный многочлен')
plt.legend()
plt.grid(True)
plt.show()


