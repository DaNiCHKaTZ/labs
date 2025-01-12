import random

def new_array(arr):
    chet = arr[1::2]  
    nechet = arr[0::2]   
    return chet + nechet

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

    new_arr = new_array(array)
    print("Массив после перестановки:", new_arr)

if __name__ == "__main__":
    main()
