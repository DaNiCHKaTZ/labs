import random

def mirror_matrix(matrix, M):
    for i in range(M):
        for j in range(M - i - 1):
            matrix[i][j], matrix[M - j - 1][M - i - 1] = matrix[M - j - 1][M - i - 1], matrix[i][j]

choice = input("Выберите способ ввода данных: ")

if choice == '1':
    M = int(input("Введите порядок матрицы (M): "))
    matrix = []
    for i in range(M):
        row = list(map(int, input("Введите элементы {}-й строки через пробел: ".format(i+1)).split()))
        matrix.append(row)
elif choice == '2':
    M = int(input("Введите порядок матрицы (M): "))
    matrix = [[random.randint(0, 100) for _ in range(M)] for _ in range(M)]
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
else:
    print("Неверный выбор!")
    matrix = []
    M = 0

if matrix:
    mirror_matrix(matrix, M)
    print("Матрица после зеркального отражения относительно побочной диагонали:")
    for row in matrix:
        print(row)
else:
    print("Матрица пуста или некорректные данные.")
