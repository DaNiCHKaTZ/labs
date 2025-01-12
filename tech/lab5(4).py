def progression(arr):
    if len(arr) < 2:
        return 0
    

    d = arr[1] - arr[0]
    
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != d:
            return 0
    
    return d

N = int(input("Введите количество элементов в массиве: "))


array = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]

difference = progression(array)
print(difference)
