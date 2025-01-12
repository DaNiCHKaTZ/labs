x = float(input("Enter x ",))
y = float(input("Enter y ",))

if x > 0 and y > 0:
    print("first")
elif x < 0 and y > 0:
    print("second")
elif x < 0 and y < 0:
    print("third")
else:
    print("fourth")
