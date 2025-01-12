import random

def insert_and_sort(B, numbers):
    numbers.append(B)
    numbers.sort()
    return numbers

def main():
    N = int(input("Введите количество элементов N: "))
    input_method = input("Выберите способ ввода данных : ")

    numbers = []
    if input_method == '1':
        for _ in range(N):
            num = float(input("Введите число: "))
            numbers.append(num)
    elif input_method == '2':
        for _ in range(N):
            num = random.uniform(0, 100) 
            numbers.append(num)
    else:
        print("Неверный выбор способа ввода данных.")
        return

    B = float(input("Введите вещественное число B: "))
    sorted_numbers = insert_and_sort(B, numbers)

    print("Отсортированный список с числом B:", sorted_numbers)

if __name__ == "__main__":
    main()
