import random

def incr(arr):
  
    last_odd = None
    for num in reversed(arr):
        if num % 2 != 0:
            last_odd = num
            break
    
 
    if last_odd is None:
        return arr
    
  
    return [num + last_odd if num % 2 != 0 else num for num in arr]

def main():
    N = int(input("Введите размер массива N: "))
    input_method = input("Выберите способ ввода данных ")

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

    new_arr = incr(array)
    print("Обновленный массив:", new_arr)

if __name__ == "__main__":
    main()
