import random

def count(arr):
    return len(set(arr))

def main():
    N = int(input("Введите размер массива N: "))
    input_method = input("Выберите способ ввода данных : ")

    array = []
    if input_method == '1':
        for _ in range(N):
            num = int(input("Введите целое число: "))
            array.append(num)
    elif input_method == '2':
        array = [random.randint(-100, 100) for _ in range(N)]  
        print("Сгенерированный массив:", array)
    else:
        print("Неверный выбор способа ввода данных.")
        return

    N = count(array)
    print("Количество различных элементов в массиве:", N)

if __name__ == "__main__":
    main()
