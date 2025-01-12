M = int(input("Введите количество строк (M): "))
N = int(input("Введите количество столбцов (N): "))


matrix = []
for i in range(M):
    row = list(map(int, input(f"Введите элементы {i + 1}-й строки через пробел: ").split()))
    matrix.append(row)


def is_positive_column(matrix, col_index):
    for row in matrix:
        if row[col_index] <= 0:
            return False
    return True


last_positive_col = -1
for j in range(N):
    if is_positive_column(matrix, j):
        last_positive_col = j


    for i in range(M):
        matrix[i][0], matrix[i][last_positive_col] = matrix[i][last_positive_col], matrix[i][0]

print("Измененная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))
