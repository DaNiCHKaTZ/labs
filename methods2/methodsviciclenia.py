import numpy as np

A = np.array([[0, -2, 2], [-1, -2, 3], [1, -3, 2]])

# Находим собственные значения и собственные векторы
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Собственные значения:")
print(eigenvalues)

print("Собственные векторы:")
print(eigenvectors)

# Находим характеристический многочлен
characteristic_polynomial = np.poly(A)
print("Характеристический многочлен:")
print(characteristic_polynomial)