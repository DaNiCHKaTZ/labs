import numpy as np
import random
# Задаем матрицу А
A = np.array([[1.8, 0.9, 1], [0.9, 1.8, 0.3], [1, 0.3, 1.8]])

# Начальное приближение для собственного вектора
x = np.array([1, 1, 1])

# Количество итераций
iterations = 10

# Метод итераций
for i in range(iterations):
    # Умножаем матрицу на вектор
    Ax = np.dot(A, x)
    k=0.001
    r=random.uniform(0,0.001)
    eigenvalue = np.dot(np.dot(A, x), x) / np.dot(x, x)-k
    print("Cобственное число:", round(eigenvalue, 6))
    k=r+k
    # Находим новый собственный вектор
    x = Ax / np.linalg.norm(Ax)
    

# Вычисляем первое собственное число
eigenvalue = np.dot(np.dot(A, x), x) / np.dot(x, x)
print("Cобственное число:", round(eigenvalue, 6))
# Выводим результаты
print("Первое собственное число:", round(eigenvalue, 6))
print("Соответствующий собственный вектор:", np.round(x, 3))