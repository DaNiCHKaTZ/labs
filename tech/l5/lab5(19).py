import random

def print_kth_row(matrix, K):
    if 1 <= K <= len(matrix):
        print("Элементы {}-й строки:".format(K), matrix[K-1])
    else:
        print("Некорректное значение K")


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
    matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
    K = int(input("Введите значение K: "))
else:
    print("Неверный выбор!")
    matrix = []
    K = 0

if matrix:
    print_kth_row(matrix, K)
