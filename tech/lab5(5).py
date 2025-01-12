N = int(input("Введите количество элементов в массиве: "))


A = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]


B = []


for i in range(0, N, 2):
    B.append(A[i])

for i in range(1, N, 2):
    B.append(A[i])


print("Новый массив B:", B)
