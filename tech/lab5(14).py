
M = int(input("Введите порядок матрицы (M): "))


matrix = []
for i in range(M):
    row = list(map(int, input(f"Введите элементы {i + 1}-й строки через пробел: ").split()))
    matrix.append(row)


def find_min_in_diagonal(matrix, start_row, start_col):
    min_element = matrix[start_row][start_col]
    row, col = start_row, start_col
    while row < M and col < M:
        if matrix[row][col] < min_element:
            min_element = matrix[row][col]
        row += 1
        col += 1
    return min_element

min_elements = []


for col in range(M):
    min_elements.append(find_min_in_diagonal(matrix, 0, col))


for row in range(1, M):
    min_elements.append(find_min_in_diagonal(matrix, row, 0))


print("Минимальные элементы диагоналей, параллельных главной:")
for i, min_element in enumerate(min_elements, 1):
    print(f"Диагональ {i}: {min_element}")
