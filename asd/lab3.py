import numpy as np

def gauss_row(matrix, vector):
    n = len(matrix)
    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[[i, max_row]] = matrix[[max_row, i]]
        vector[[i, max_row]] = vector[[max_row, i]]
        for j in range(i+1, n):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j][i] = 0
            for k in range(i+1, n):
                matrix[j][k] -= factor * matrix[i][k]
            vector[j] -= factor * vector[i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (vector[i] - np.dot(matrix[i][i+1:], x[i+1:])) / matrix[i][i]
    return x
def gauss_column(matrix, vector):
    n = len(matrix)
    for i in range(n):
        max_col = i
        for j in range(i+1, n):
            if abs(matrix[i][j]) > abs(matrix[i][max_col]):
                max_col = j
        matrix[:, [i, max_col]] = matrix[:, [max_col, i]]
        vector[[i, max_col]] = vector[[max_col, i]]
        for j in range(i+1, n):
            factor = matrix[i][j] / matrix[i][i]
            matrix[i][j] = 0
            for k in range(i+1, n):
                matrix[k][j] -= factor * matrix[k][i]
            vector[j] -= factor * vector[i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (vector[i] - np.dot(matrix[i][i+1:], x[i+1:])) / matrix[i][i]
    return x

def gauss_matrix(matrix, vector):
    n = len(matrix)
    for i in range(n):
        max_row, max_col = np.unravel_index(np.abs(matrix[i:, i:]).argmax(), matrix[i:, i:].shape)
        max_row += i
        max_col += i
        matrix[[i, max_row]] = matrix[[max_row, i]]
        matrix[:, [i, max_col]] = matrix[:, [max_col, i]]
        vector[[i, max_row]] = vector[[max_row, i]]
        for j in range(i+1, n):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j][i] = 0
            for k in range(i+1, n):
                matrix[j][k] -= factor * matrix[i][k]
            vector[j] -= factor * vector[i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (vector[i] - np.dot(matrix[i][i+1:], x[i+1:])) / matrix[i][i]
    return x
# Пример использования
A = np.array([[2, 1, -1], 
              [-3, -1, 2], 
              [-2, 1, 2]])
b = np.array([8, -11, -3])

#x = gauss_row(A, b)
x = gauss_matrix(A,b)
#x = gauss_column(A,b)
print("Решение:")
print(x)
