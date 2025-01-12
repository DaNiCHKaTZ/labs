N = int(input("Введите количество элементов в массиве: "))

array = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]

last_elem = {}
for i in range(N):
    last_elem[array[i]] = i


result = [array[i] for i in range(N) if last_elem[array[i]] == i]


print("Массив без дубликатов, оставляя последние вхождения:", result)
