import numpy as np

def gaussian_elimination(matrix):
    n = len(matrix)
    
    for i in range(n): 
        # Выбор главного элемента
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[[i, max_row]] = matrix[[max_row, i]] # обмен строк
        
        # Приведение матрицы к ступенчатому виду (элементы ниже главной диагонали обнуляются)
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] -= factor * matrix[i]
    
    # Обратный проход
    solution = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solution[i] = (matrix[i][n] - np.dot(matrix[i][i + 1:n], solution[i + 1:n])) / matrix[i][i]
    
    return solution

# Пример использования
matrix = np.array([[3, 2, -4, 3],
                   [2, 3, 3, 15],
                   [5, -3, 1, 14]])

solution = gaussian_elimination(matrix)
print("Решение:", solution)