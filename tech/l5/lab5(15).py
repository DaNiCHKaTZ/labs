def update(arr):
    for i in range(1, len(arr), +2):
        arr[i]*=3
    return arr


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
    result = update(arr)
    print("Массив после обновления:", result)
else:
    print("Массив пуст.")
