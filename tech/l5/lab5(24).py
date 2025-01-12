import random

def swap(matrix, M, N):
    half_M, half_N = M // 2, N // 2
    for i in range(half_M):
        for j in range(half_N):
            matrix[i][j], matrix[i + half_M][j + half_N] = matrix[i + half_M][j + half_N], matrix[i][j]

choice = input("Выберите способ ввода данных : ")

if choice == '1':
    M = int(input("Введите количество строк (M): "))
    N = int(input("Введите количество столбцов (N): "))
    matrix = []
    for i in range(M):
        row = list(map(int, input("Введите элементы {}-й строки через пробел: ".format(i+1)).split()))
        matrix.append(row)
elif choice == '2':
    M = int(input("Введите количество строк (M): "))
    N = int(input("Введите количество столбцов (N): "))
    matrix = [[random.randint(0, 100) for _ in range(N)] for _ in range(M)]
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
else:
    print("Неверный выбор!")
    matrix = []
    M = N = 0

if matrix and M % 2 == 0 and N % 2 == 0:
    swap(matrix, M, N)
    print("Матрица после замены четвертей:")
    for row in matrix:
        print(row)
else:
    print("Некорректные данные или размеры матрицы нечетные.")
