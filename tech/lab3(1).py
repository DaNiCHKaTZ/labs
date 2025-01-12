x = float(input("Enter x: "))
n = int(input("Enter n: "))
f = 0

for i in range(1, n + 1):
    step = ((-1)**(i+1)) * (x**i) / i
    f += step

print(f)