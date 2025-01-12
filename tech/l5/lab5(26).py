import random

def sort_col(matrix):
    last_elements = [(matrix[-1][j], j) for j in range(len(matrix[0]))]
    last_elements.sort(reverse=True, key=lambda x: x[0])
    sorted_matrix = [[row[j] for _, j in last_elements] for row in matrix]
    return sorted_matrix

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
    sorted_matrix = sort_col(matrix)
    print("Матрица после сортировки столбцов по последним элементам в убывающем порядке:")
    for row in sorted_matrix:
        print(row)
else:
    print("Матрица пуста или некорректные данные.")
