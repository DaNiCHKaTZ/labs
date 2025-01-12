import numpy as np

x = int(input("x = ", ))
y = int(input("y = ", ))
m = 20
n = 10**6

a = np.random.randint(1, m + 1, n)
b = np.random.randint(1, m + 1, n)

ysl = (y < a + b) & (a + b <= 2 * y) & (b == 2 * x)

count = np.sum(ysl)

print(f'Количество индексов, удовлетворяющих условию: {count}')
