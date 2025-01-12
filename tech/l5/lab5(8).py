import random

def count(arr):
    count = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] < arr[i + 1]:
            count += 1
            while i < len(arr) - 1 and arr[i] < arr[i + 1]:
                i += 1
        i += 1
    return count

def main():
    N = int(input("Введите размер массива N: "))
    input_method = input("Выберите способ ввода данных : ")

    array = []
    if input_method == '1':
        for _ in range(N):
            num = float(input("Введите число: "))
            array.append(num)
    elif input_method == '2':
        array = [random.uniform(0, 100) for _ in range(N)]  
        print("Сгенерированный массив:", array)
    else:
        print("Неверный выбор способа ввода данных.")
        return

    incr = count(array)
    print("Количество участков, на которых элементы массива возрастают:", incr)

if __name__ == "__main__":
    main()
