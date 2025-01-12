class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, key):
        return (self.hash_function(key) + 1) % self.size

    def put(self, key, data):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(key)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash_function(key)
        position = start_slot

        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    break
                return None
        
    def print_table(self):
        for i in range(self.size):
            if self.slots[i] is not None:
                print(f"Key: {self.slots[i]}, Data: {self.data[i]}")


import time
import random

# Создание хеш-таблицы
ht = HashTable(1000000)

# for i in range(10): # Заполнение хеш-таблицы случайными значениями
#     key = random.randint(1, 10)
#     data = random.randint(1, 10)
#     ht.put(key, data)
# ht.print_table()

ht.put(10,2)

key_to_find = int(input())
start_time = time.process_time()
found_data = ht.get(key_to_find)
end_time = time.process_time()

if found_data is not None:
    print(f"Element with key {key_to_find} found. Data: {found_data}")
else:
    print(f"Element with key {key_to_find} not found.")

execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
# numbers = random.sample(range(1, 10000000), n)
# start_time = time.time()
# for number in numbers:
#     ht.put(number, number)
# elapsed_time = time.time() - start_time
# print(f"Добавление первых {n} чисел: {elapsed_time} сек")

# start_time = time.time()
# for number in numbers:
#     ht.get(number)
# elapsed_time = time.time() - start_time
# print(f"Поиск первых {n} чисел: {elapsed_time} сек")

# numbers = random.sample(range(1, 10000000), n)

# start_time = time.time()
# for number in numbers:
#     ht.put(number, number)
# elapsed_time = time.time() - start_time
# print(f"Добавление последних {n} чисел: {elapsed_time} сек")


# # Замеры для n=10000
# n = 10000
# numbers = random.sample(range(1, 10000000), n)

# start_time = time.time()
# for number in numbers:
#     ht.put(number, number)
# elapsed_time = time.time() - start_time
# print(f"Добавление первых {n} чисел: {elapsed_time} сек")

# start_time = time.time()
# for number in numbers:
#     ht.get(number)
# elapsed_time = time.time() - start_time
# print(f"Поиск первых {n} чисел: {elapsed_time} сек")

# numbers = random.sample(range(1, 10000000), n)

# start_time = time.time()
# for number in numbers:
#     ht.put(number, number)
# elapsed_time = time.time() - start_time
# print(f"Добавление последних {n} чисел: {elapsed_time} сек")

# # Замеры для n=100000
# n = 100000
# numbers = random.sample(range(1, 10000000), n)

# start_time = time.time()
# for number in numbers:
#     ht.put(number, number)
# elapsed_time = time.time() - start_time
# print(f"Добавление первых {n} чисел: {elapsed_time} сек")

# start_time = time.time()
# for number in numbers:
#     ht.get(number)
# elapsed_time = time.time() - start_time
# print(f"Поиск первых {n} чисел: {elapsed_time} сек")

# numbers = random.sample(range(1, 10000000), n)

# start_time = time.time()
# for number in numbers:
#     ht.put(number, number)
# elapsed_time = time.time() - start_time
# print(f"Добавление последних {n} чисел: {elapsed_time} сек")