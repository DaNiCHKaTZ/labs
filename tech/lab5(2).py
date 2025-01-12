K = int(input("K = "))
N = int(input("N = "))

results = []


for i in range(K):
    print(f"Набор {i+1}:")
    last_index = 0
    for j in range(N):
        num = int(input(f"Введите элемент {j+1}: "))
        if num == 2:
            last_index = j + 1
    results.append(last_index)


for i, result in enumerate(results, 1):
    print(f"Последний элемент равный 2, в наборе {i}: {result}")
