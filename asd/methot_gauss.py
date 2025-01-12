import numpy as np

def gauss_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        # Выбор главного элемента в зависимости от выбранного метода
        if method == '1':  # По строке
            pivot_row = i
            pivot_col = np.argmax(np.abs(matrix[i:, i])) + i
        elif method == '2':  # По столбцу
            pivot_row = np.argmax(np.abs(matrix[i:, i])) + i
            pivot_col = i
        elif method == '3':  # По матрице
            pivot_row, pivot_col = np.unravel_index(np.abs(matrix[i:, i:]).argmax(), matrix[i:, i:].shape)
            pivot_row += i
            pivot_col += i
            
        # Перестановка строк для выбора главного элемента
        matrix[[i, pivot_row]] = matrix[[pivot_row, i]]
        
        # Приведение матрицы к треугольному виду
        for j in range(i + 1, n):
            factor = matrix[j, i] / matrix[i, i]
            matrix[j, i:] -= factor * matrix[i, i:]
    
    return matrix

# Ввод размерности матрицы
n = int(input("Введите размерность матрицы: "))

# Ввод элементов матрицы
matrix = np.zeros((n, n + 1))
for i in range(n):
    print("\nВведите элементы {0}-й строки матрицы:".format(i + 1))
    for j in range(n + 1):
        matrix[i, j] = float(input("Элемент {0}: ".format(j + 1)))

# Ввод метода решения
method = input("\nВыберите метод решения (1 - по строке, 2 - по столбцу, 3 - по матрице): ")

# Вызов функции для решения методом Гаусса с выбором главного элемента
result = gauss_elimination(matrix)

# Вывод результата
print("\nРезультат применения метода Гаусса с выбором главного элемента:")
for i in range(n):
    print("x{0} = {1}".format(i + 1, result[i, -1] / result[i, i]))
