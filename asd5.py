import heapq
import os
import time
import random
import io

def merge_files(filenames, output_file):
    count_comparisons = 0
    count_file_accesses = 0
    with open(output_file, 'w') as output:
        heap = []
        files = [open(filename, 'r') for filename in filenames]
        
        for i, file in enumerate(files):
            line = file.readline()
            count_file_accesses += 1
            if line:
                heapq.heappush(heap, (int(line), i))
        
        while heap:
            smallest, file_index = heapq.heappop(heap)
            count_comparisons += 1
            output.write(str(smallest) + '\n')
            
            line = files[file_index].readline()
            count_file_accesses += 1
            if line:
                heapq.heappush(heap, (int(line), file_index))
            
        

    for file in files:
        file.close()

    return count_comparisons, count_file_accesses

    
    
            
        

    
 

def external_sort(input_file, output_file, chunk_size=1000):
    count_comparisons = 0
    count_file_accesses = 0
    filenames = []
    with open(input_file, 'r') as input:
        chunk = []
        i = 0
        for line in input:
            chunk.append(int(line))
            if len(chunk) >= chunk_size:
                count_comparisons += chunk_size * (chunk_size - 1) / 2
                count_file_accesses += 1
                chunk.sort()
                filename = f'temp_{i}.txt'
                filenames.append(filename)
                with open(filename, 'w') as temp:
                    for num in chunk:
                        temp.write(str(num) + '\n')
                        count_file_accesses += 1
                        
                chunk = []
                i += 1
        
        if chunk:
            count_comparisons += len(chunk) * (len(chunk) - 1) / 2
            count_file_accesses += 1
            chunk.sort()
            filename = f'temp_{i}.txt'
            filenames.append(filename)
            with open(filename, 'w') as temp:
                for num in chunk:
                    temp.write(str(num) + '\n')
                    count_file_accesses += 1
                  

    while len(filenames) > 1:
        merged_filenames = []
        for i in range(0, len(filenames), 3):
            chunk = filenames[i:i+3]
            merged_filename = f'merged_{i//3}.txt'
            merged_filenames.append(merged_filename)
            merge_comparisons, merge_file_accesses = merge_files(chunk, merged_filename)
            count_comparisons += merge_comparisons
            count_file_accesses += merge_file_accesses
        
        filenames = merged_filenames

    final_filename = filenames[0]
    os.rename(final_filename, output_file)
    print (count_comparisons)
    print (count_file_accesses)
    return count_comparisons, count_file_accesses

    
with open("input3.txt", "w") as file:
     for num in range(10, 0, -1):
        file.write(str(num) + "\n")


file1 = io.open('input1.txt', 'w')
for i in range(10):
    random_number = random.randint(1, 100)
    file1.write(str(random_number))
    file1.write('\n')

# Закрыть файл
file1.close()

# Пример использования
input_file = 'input1.txt'
output_file = 'output.txt'
start_time = time.time()
external_sort(input_file, output_file)
print("--- %s seconds ---" % (time.time() - start_time))