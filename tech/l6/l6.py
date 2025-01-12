import random
import copy

class Matrix:
    def __init__(self, rows=0, cols=0, element_type=float):
        self.__element_type = element_type
        if rows == 0 and cols == 0:
            self.__init_default()
        else:
            self.__init_with_random(rows, cols)
        self.__rows = rows
        self.__cols = cols

    def __init_default(self):
        self.__matrix = []
        self.__rows = 0
        self.__cols = 0

    def __init_with_random(self, rows, cols):
        self.__matrix = [[self.__element_type(random.uniform(0, 100)) for _ in range(cols)] for _ in range(rows)]
        self.__rows = rows
        self.__cols = cols

    def __copy__(self):
        new_matrix = Matrix(self.__rows, self.__cols, self.__element_type)
        new_matrix.__matrix = [row[:] for row in self.__matrix]
        return new_matrix

    def get_element(self, row, col):
        return self.__matrix[row][col]

    def set_element(self, row, col, value):
        self.__matrix[row][col] = self.__element_type(value)

    def get_size(self):
        return self.__rows, self.__cols

    def get_element_count(self):
        return self.__rows * self.__cols

    def get_element_type(self):
        return self.__element_type

    def __str__(self):
        return '\n'.join([' '.join(f"{value:.2f}" for value in row) for row in self.__matrix])

    def up(self):
        if self.__rows > 1:
            first_row = self.__matrix.pop(0)
            self.__matrix.append(first_row)

    def __neg__(self):
        self.up()
        return self

def read_input(file_path):
    with open(file_path, 'r') as file:
        rows, cols = map(int, file.readline().split())
        element_type_str = file.readline().strip()
        
        if element_type_str == "int":
            element_type = int
        elif element_type_str == "float":
            element_type = float
        else:
            raise ValueError(f"Неверный тип данных: {element_type_str}")
            
    return rows, cols, element_type

def write_output(file_path, matrix):
    with open(file_path, 'w') as file:
        file.write(str(matrix))


rows, cols, element_type = read_input('input.txt')
matrix = Matrix(rows, cols, element_type)
print("\nИсходная матрица:")
print(matrix)

matrix.set_element(1, 1, 14.5)
print("Новый элемент (1,1) =", matrix.get_element(1, 1))
print(matrix)

matrix_copy = copy.copy(matrix)
print("\nКопия матрицы:")
print(matrix_copy)

-matrix
print("\nМатрица после циклического сдвига строк вверх:")
print(matrix)

print("\nКоличество элементов в матрице:", matrix.get_element_count())
print("Тип элементов в матрице:", matrix.get_element_type())

write_output('output.txt', matrix)
