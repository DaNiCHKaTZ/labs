import random

def reverse(arr):
    return arr[::-1]

def main():
    N = int(input("Введите размер массива N: "))
    in_m = input("Выберите способ ввода данных : ")

    array = []
    if in_m == '1':
        for _ in range(N):
            num = float(input("Введите число: "))
            array.append(num)
    elif in_m == '2':
        array = [random.uniform(0, 100) for _ in range(N)] 
        print("Сгенерированный массив:", array)
    else:
        print("Неверный выбор способа ввода данных.")
        return

    r_arr = reverse(array)
    print("Массив в обратном порядке:", r_arr)

if __name__ == "__main__":
    main()
