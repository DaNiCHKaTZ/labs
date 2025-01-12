a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
x1 = float(input("Enter first x: "))
x2 = float(input("Enter last x: "))
h = float(input("Enter шаг: "))

x_val = []
f_val = []

x = x1
while x <= x2:
    if a < 0 and x != 0:
        fx = a * x * x + b * b * x
    elif a > 0 and x == 0:
        fx = x - a / (x - c)
    else:
        fx = 1 + x / c
    f_val.append(fx)
    x_val.append(x)
    x += h

print("x       f(x)")
print("----------------")
for i in range(len(x_val)):
    print(f"{x_val[i]:<8.3f} {f_val[i]:<8.3f}")
