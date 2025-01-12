import random
import numpy as np

def sum_and_product(matrix, K):
    row = matrix[K-1]
    row_sum = sum(row)
    row_product = np.prod(row)
    return row_sum, row_product

choice = input("Выберите способ ввода данных : ")

if choice == '1':
    M = int(input("Введите количество строк (M): "))
    N = int(input("Введите количество столбцов (N): "))
    matrix = []
    for i in range(M):
        row = list(map(int, input("Введите элементы {}-й строки через пробел: ".format(i+1)).split()))
        matrix.append(row)
    K = int(input("Введите значение K: "))
elif choice == '2':
    M = int(input("Введите количество строк (M): "))
    N = int(input("Введите количество столбцов (N): "))
    matrix = [[random.randint(1, 10) for _ in range(N)] for _ in range(M)]
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
    K = int(input("Введите значение K: "))
else:
    print("Неверный выбор!")
    matrix = []
    K = 0

if matrix and 1 <= K <= M:
    row_sum, row_product = sum_and_product(matrix, K)
    print("Сумма элементов {}-й строки: {}".format(K, row_sum))
    print("Произведение элементов {}-й строки: {}".format(K, row_product))
else:
    print("Некорректные данные или значение K.")
