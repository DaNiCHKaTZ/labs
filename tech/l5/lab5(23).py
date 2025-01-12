import random

def swap(matrix, K1, K2):
    matrix[K1-1], matrix[K2-1] = matrix[K2-1], matrix[K1-1]


choice = input("Выберите способ ввода данных : ")

if choice == '1':
    M = int(input("Введите количество строк (M): "))
    N = int(input("Введите количество столбцов (N): "))
    matrix = []
    for i in range(M):
        row = list(map(int, input("Введите элементы {}-й строки через пробел: ".format(i+1)).split()))
        matrix.append(row)
    K1 = int(input("Введите значение K1: "))
    K2 = int(input("Введите значение K2: "))
elif choice == '2':
    M = int(input("Введите количество строк (M): "))
    N = int(input("Введите количество столбцов (N): "))
    matrix = [[random.randint(0, 100) for _ in range(N)] for _ in range(M)]
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
    K1 = int(input("Введите значение K1: "))
    K2 = int(input("Введите значение K2: "))
else:
    print("Неверный выбор!")
    matrix = []
    K1 = K2 = 0

if matrix and 1 <= K1 < K2 <= M:
    swap(matrix, K1, K2)
    print("Матрица после замены строк {} и {}:".format(K1, K2))
    for row in matrix:
        print(row)
else:
    print("Некорректные данные или значения K1 и K2.")
