import numpy as np
from scipy.integrate import solve_ivp

def func(x, y):
    return 1 + (1 - x) * np.sin(y) - (2 + x) * y

x0 = 0
y0 = [0]
h = 0.1
x = np.arange(0, 1+h, h)

sol = solve_ivp(func, [x0, 1], y0, method='RK45', t_eval=x)

for i in range(3, len(x)):
    y_next = sol.y[0][i-1] + h/24 * (55*func(x[i-1], sol.y[0][i-1]) - 59*func(x[i-2], sol.y[0][i-2]) + 37*func(x[i-3], sol.y[0][i-3]) - 9*func(x[i-4], sol.y[0][i-4]))
    sol.y[0][i] = y_next

for i in range(len(x)):
    print(f"x = {x[i]:.1f}, y = {sol.y[0][i]:.4f}")
