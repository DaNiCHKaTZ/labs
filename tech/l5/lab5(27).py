import random

def max_elem(matrix, M):
    max_elements = []
    
    for start in range(M):
        max_element = matrix[start][0]
        i, j = start, 0
        while i >= 0 and j < M:
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
            i -= 1
            j += 1
        max_elements.append(max_element)

    for start in range(1, M):
        max_element = matrix[M-1][start]
        i, j = M-1, start
        while i >= 0 and j < M:
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
            i -= 1
            j += 1
        max_elements.append(max_element)
    
    return max_elements


choice = input("Выберите способ ввода данных : ")

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
    max_elements = max_elem(matrix, M)
    print("Максимальные элементы диагоналей, параллельных побочной диагонали:")
    for elem in max_elements:
        print(elem)
else:
    print("Матрица пуста или некорректные данные.")
