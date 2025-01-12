import random

def remove(matrix):
    columns = []
    for j in range(len(matrix[0])):
        if any(matrix[i][j] <= 0 for i in range(len(matrix))):
            columns.append(j)
    
    new_matrix = [[matrix[i][j] for j in columns] for i in range(len(matrix))]
    return new_matrix


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
    matrix = [[random.randint(-50, 50) for _ in range(N)] for _ in range(M)]
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
else:
    print("Неверный выбор!")
    matrix = []

if matrix:
    new_matrix = remove(matrix)
    print("Матрица после удаления столбцов с только положительными элементами:")
    for row in new_matrix:
        print(row)
else:
    print("Матрица пуста или некорректные данные.")
