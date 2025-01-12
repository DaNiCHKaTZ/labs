import random
import time

def selection_sort(array):
    comparisons = 0
    swaps = 0
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            comparisons += 1
            if array[j] < array[min_index]:
                min_index = j
                swaps += 1
        array[i], array[min_index] = array[min_index], array[i]
        
    print("Количество сравнений:", comparisons)
    print("Количество обменов:", swaps)
    return array



def insertion_sort(array):
    k = 0 
    s = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
            s = s + 1
        array[j+1] = key
        k = k+1
    print ("Compare ", k)
    print ("Swap ", s)
    return array




def bubble_sort(array):
    comparisons = 0
    swaps = 0
    for i in range(len(array) - 1, 0, -1):
        comparisons += 1
        no_swap = True
        for j in range(0, i):
            comparisons += 1
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps += 1
                comparisons += 1
                no_swap = False
        if no_swap:
            break
    
    print("Количество сравнений:", comparisons)
    print("Количество обменов:", swaps)
    return array
 

def quickSort(array):
    comparisons = 0
    swaps = 0

    def partition(array, low, high):
        nonlocal comparisons, swaps
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                swaps += 1
        array[i + 1], array[high] = array[high], array[i + 1]
        swaps += 1
        return i + 1

    def quickSortHelper(array, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pi = partition(array, low, high)
            quickSortHelper(array, low, pi - 1)
            quickSortHelper(array, pi + 1, high)

    quickSortHelper(array, 0, len(array) - 1)

    print("Количество сравнений:", comparisons)
    print("Количество обменов:", swaps)
    return array

def timsort(array):
    comparisons = 0
    swaps = 0

    def insertion_sort(array, left, right):
        nonlocal comparisons, swaps
        for i in range(left + 1, right + 1):
            key_item = array[i]
            j = i - 1
            while j >= left and array[j] > key_item:
                comparisons += 1
                array[j + 1] = array[j]
                swaps += 1
                j -= 1
            array[j + 1] = key_item

    def merge(array, left, mid, right):
        nonlocal comparisons, swaps
        len_left = mid - left + 1
        len_right = right - mid
        left_arr = array[left:mid + 1]
        right_arr = array[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len_left and j < len_right:
            comparisons += 1
            if left_arr[i] <= right_arr[j]:
                array[k] = left_arr[i]
                swaps += 1
                i += 1
            else:
                array[k] = right_arr[j]
                swaps += 1
                j += 1
            k += 1

        while i < len_left:
            array[k] = left_arr[i]
            swaps += 1
            i += 1
            k += 1

        while j < len_right:
            array[k] = right_arr[j]
            swaps += 1
            j += 1
            k += 1

    def timsort_helper(array, left, right):
        nonlocal comparisons, swaps
        if right - left + 1 <= 32:
            insertion_sort(array, left, right)
            return

        mid = (left + right) // 2
        timsort_helper(array, left, mid)
        timsort_helper(array, mid + 1, right)
        merge(array, left, mid, right)

    timsort_helper(array, 0, len(array) - 1)

    print("Количество сравнений:", comparisons)
    print("Количество обменов:", swaps)
    return array    

    





array=list(range(1,1000,1))
array1=list(range(1000,0,-1))
array2=[random.randint(-100000,100000) for _ in range(1000)]
start_time = time.time()
timsort(array2)
print("--- %s seconds ---" % (time.time() - start_time))


