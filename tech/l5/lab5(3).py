def new_num(num):
    new = []
    for i in range(len(num)):
        if i == 0:
            new.append(num[i])
        else:
            new.append(num[i] ** (i + 1))
    return new

def main():
    N = int(input("Введите количество элементов N: "))
    input_method = input("Выберите способ ввода данных : ")

    numbers = []
    if input_method == '1':
        for _ in range(N):
            num = float(input("Введите число: "))
            numbers.append(num)
    elif input_method == '2':
        import random
        for _ in range(N):
            num = random.uniform(0, 100)  
            numbers.append(num)
        print(numbers)
    else:
        print("Неверный выбор способа ввода данных.")
        return

    transformed_numbers = new_num(numbers)
    print("Преобразованные числа:", transformed_numbers)

if __name__ == "__main__":
    main()
