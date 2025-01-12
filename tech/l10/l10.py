import numpy as np

mu = 0.1
sigma = 0.2

n = 10**6

a = np.random.normal(mu, sigma, n)

a = np.clip(a, -1, 1)

def f(x):
    return np.arcsin(x - 0.1)**2

b = np.where((a - 0.1 >= -1) & (a - 0.1 <= 1), f(a), 0)

srznach = np.mean(b)
disp = np.var(b)
mediana = np.median(b)
min = np.min(b)
max = np.max(b)

print(f'Среднее значение: {srznach}')
print(f'Дисперсия: {disp}')
print(f'Медиана: {mediana}')
print(f'Минимальный элемент: {min}')
print(f'Максимальный элемент: {max}')
