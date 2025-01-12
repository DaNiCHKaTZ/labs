N = int(input("Введите количество элементов в массиве: "))

array = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]


for i in range(N // 2):
    array[i], array[N - i - 1] = array[N - i - 1], array[i]

print("Массив в обратном порядке:", array)
