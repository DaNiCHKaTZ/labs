import numpy as np

N = int(input("N = "))


array = np.zeros(N, dtype=int)


for i in range(N):
    array[i] = int(input())


print(" ")

while N > 0:
    print(array[N-1])
    N -= 1
