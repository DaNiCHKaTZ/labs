def remove(arr, K):

    series_count = 0
    i = 0
    
    while i < len(arr):
        
        start = i
        while i < len(arr) - 1 and arr[i] == arr[i + 1]:
            i += 1
     
        end = i
        
       
        series_count += 1
        
     
        if series_count == K:
            arr = arr[:start] + arr[end + 1:]
            break
        
        i += 1
    
    return arr


N = int(input("Введите количество элементов в массиве: "))
K = int(input("Введите номер серии для удаления: "))


array = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]


result = remove(array, K)

print("Массив после удаления серии:", result)
