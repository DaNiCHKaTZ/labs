import random

def find(arr):
    minimum = []
    n = len(arr)
    for i in range(n):
        if (i == 0 and arr[i] < arr[i + 1]) or \
           (i == n - 1 and arr[i] < arr[i - 1]) or \
           (0 < i < n - 1 and arr[i] < arr[i - 1] and arr[i] < arr[i + 1]):
            minimum.append(i)
    return minimum

def update(arr):
    min = find(arr)
    for i in min:
        arr[i] = arr[i] ** 2
    return arr

def main():
    N = int(input("Введите размер массива N: "))
    input_method = input("Выберите способ ввода данных : ")

    array = []
    if input_method == '1':
        for _ in range(N):
            num = int(input("Введите целое число: "))
            array.append(num)
    elif input_method == '2':
        array = [random.randint(-100, 100) for _ in range(N)]  # Генерация случайных целых чисел от -100 до 100
        print("Сгенерированный массив:", array)
    else:
        print("Неверный выбор способа ввода данных.")
        return

    new_array = update(array)
    print("Обновленный массив:", new_array)

if __name__ == "__main__":
    main()
