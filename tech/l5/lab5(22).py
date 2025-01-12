import random

def count(matrix):
    last_column = set(matrix[i][-1] for i in range(len(matrix)))
    count = 0
    for j in range(len(matrix[0]) - 1):
        column_set = set(matrix[i][j] for i in range(len(matrix)))
        if column_set == last_column:
            count += 1
    return count


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

if matrix:
    similar = count(matrix)
    print("Количество столбцов, похожих на последний столбец:", similar)
else:
    print("Матрица пуста или некорректные данные.")
