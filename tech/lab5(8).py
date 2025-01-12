N = int(input("Введите количество элементов в массиве (не более 6): "))


A = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]


for i in range(1, N):
    key = A[i]
    j = i - 1
   
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key

    print(f"Массив после обработки элемента {i + 1}: {A}")


print("Отсортированный массив:", A)
