import random

def check(arr):
    for i in range(1, len(arr)):
        if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
            return i + 1   
    return 0

def main():
    N = int(input("Введите размер массива N: "))
    input_method = input("Выберите способ ввода данных : ")

    array = []
    if input_method == '1':
        for _ in range(N):
            num = int(input("Введите ненулевое целое число: "))
            array.append(num)
    elif input_method == '2':
        array = [random.randint(-100, 100) for _ in range(N) if random.randint(-100, 100) != 0]  # Генерация случайных ненулевых целых чисел
        print("Сгенерированный массив:", array)
    else:
        print("Неверный выбор способа ввода данных.")
        return

    result = check(array)
    if result == 0:
        print("Числа чередуются. Результат: 0")
    else:
        print(f"Числа не чередуются. Порядковый номер первого элемента, нарушающего закономерность: {result}")

if __name__ == "__main__":
    main()
