def update(arr, L):
    result = []
    i = 0
    while i < len(arr):
        count = 1
        while i + count < len(arr) and arr[i] == arr[i + count]:
            count += 1
        if count > L:
            result.append(0)
        else:
            result.extend(arr[i:i + count])
        i += count
    return result


choice = input("Выберите способ ввода данных : ")

if choice == '1':
    arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
    L = int(input("Введите значение L: "))
elif choice == '2':
    import random
    N = int(input("Введите размер массива: "))
    L = int(input("Введите значение L: "))
    arr = [random.randint(1, 5) for _ in range(N)]
    print("Сгенерированный массив:", arr)
else:
    print("Неверный выбор!")
    arr = []
    L = 0

if len(arr) > 0 and L > 0:
    result = update(arr, L)
    print("Массив после замены длинных серий на нули:", result)
else:
    print("Массив пуст или значение L некорректно.")
