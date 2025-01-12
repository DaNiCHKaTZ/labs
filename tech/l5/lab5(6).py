def new_arr(arr):
    result = []
    left = 0
    right = len(arr) - 1
    while left <= right:
        if left <= right:
            result.append(arr[left])
            left += 1
        if left <= right:
            result.append(arr[left])
            left += 1
        if left <= right:
            result.append(arr[right])
            right -= 1
        if left <= right:
            result.append(arr[right])
            right -= 1
    return result

def main():
    N = int(input("Введите размер массива N: "))
    in_m = input("Выберите способ ввода данных (1 - вручную, 2 - случайно): ")
    array = []
    if in_m == '1':
        for _ in range(N):
            num = float(input("Введите число: "))
            array.append(num)
    elif in_m == '2':
        import random
        array = [random.uniform(0, 100) for _ in range(N)]
        print("Сгенерированный массив:", array)
    else:
        print("Неверный выбор способа ввода данных.")
        return
    ordered_array = new_arr(array)
    print("Массив в указанном порядке:", ordered_array)

if __name__ == "__main__":
    main()
