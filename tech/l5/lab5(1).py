import random

def main():
    N = int(input("N = "))

    numbers = []
    sum = 0

    input_method = input("Выберите способ ввода данных: ")

    if input_method == '1':
        for _ in range(N):
            num = float(input("Введите число: "))
            rounded_num = round(num)
            numbers.append(rounded_num)
            sum += rounded_num
    elif input_method == '2':
        for _ in range(N):
            num = random.uniform(0, 100)  
            print(num)
            rounded_num = round(num)
            numbers.append(rounded_num)
            sum += rounded_num
    else:
        print("Неверный выбор способа ввода данных.")
        return

    print("Округленные числа:", numbers)
    print("Сумма округленных чисел:", sum)

if __name__ == "__main__":
    main()