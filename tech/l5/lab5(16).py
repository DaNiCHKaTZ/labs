def insert(arr):
   
    result = [0, arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(0)
        result.append(arr[i])
    return result


choice = input("Выберите способ ввода данных (1 - с клавиатуры, 2 - случайные числа): ")

if choice == '1':
    arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
elif choice == '2':
    import random
    N = int(input("Введите размер массива: "))
    arr = [random.randint(1, 20) for _ in range(N)]
    print("Сгенерированный массив:", arr)
else:
    print("Неверный выбор!")
    arr = []

if len(arr) > 0:

    result = insert(arr)
    print("Массив после вставки нулей:", result)
else:
    print("Массив пуст.")
