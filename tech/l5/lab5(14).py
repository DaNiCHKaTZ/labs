def remove(arr):
    seen = {}
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] not in seen:
            seen[arr[i]] = i
    return [arr[i] for i in sorted(seen.values())]


choice = input("Выберите способ ввода данных : ")

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
    result = remove(arr)
    print("Массив после удаления дубликатов:", result)
else:
    print("Массив пуст.")
