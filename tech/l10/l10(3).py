import numpy as np


n = 10**5
m = 50


a = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        a[i, j] = (5 * m * j + 5 * i - 3) / n


medians = np.median(a, axis=0)


max_median = np.max(medians)
min_median = np.min(medians)
sred_median = np.mean(medians)
sred_otk_median = np.std(medians)


print(f'Максимальная медиана: {max_median}')
print(f'Минимальная медиана: {min_median}')
print(f'Среднее значение медиан: {sred_median}')
print(f'Среднеквадратическое отклонение медиан: {sred_otk_median}')
