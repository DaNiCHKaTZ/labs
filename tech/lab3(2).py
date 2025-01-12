n = int(input("Enter n: "))
t = False
k=0
while n > 0:
    if n % 2 != 0:
        t = True
        break
    n = n // 10  


print(t)
