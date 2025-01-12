import random

def max_of_min(matrix):
    min_elements = [min(row) for row in matrix]
    return max(min_elements)


choice = input("Выберите способ ввода данных  ")

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
    matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
else:
    print("Неверный выбор!")
    matrix = []

if matrix:
    result = max_of_min(matrix)
    print("Максимальный среди минимальных элементов строк:", result)
else:
    print("Матрица пуста или некорректные данные.")
