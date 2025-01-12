import random

def insert(arr):
    first_el = arr.pop(0)
    for i in range(len(arr)):
        if arr[i] > first_el:
            arr.insert(i, first_el)
            break
    else:
        arr.append(first_el)
    return arr

def main():
    choice = input("Выберите способ ввода данных : ")
    
    if choice == '1':
        arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
    elif choice == '2':
        N = int(input("Введите размер массива: "))
        arr = [random.randint(1, 100) for _ in range(N)]
        print("Сгенерированный массив:", arr)
    else:
        print("Неверный выбор!")
        return
    
    if len(arr) > 1:
        sorted_arr = insert(arr)
        print("Упорядоченный массив:", sorted_arr)
    else:
        print("Массив слишком мал для сортировки.")

if __name__ == "__main__":
    main()
