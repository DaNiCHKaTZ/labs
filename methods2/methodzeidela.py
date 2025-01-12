def zeidel_method(x1, x2, x3, epsilon=0.0001):
    while True:
        new_x1 = (2.5 + 3.5*x2 - 0.4*x3) / 4.5
        new_x2 = (-1.5 - 3.1*new_x1 + 2.3*x3) / -8.6
        new_x3 = (6.4 - 0.8*new_x1 - 2.4*new_x2) / -7.5
        
        if abs(new_x1 - x1) < epsilon and abs(new_x2 - x2) < epsilon and abs(new_x3 - x3) < epsilon:
            return new_x1, new_x2, new_x3
        
        x1, x2, x3 = new_x1, new_x2, new_x3

x1, x2, x3 = zeidel_method(0, 0, 0)
print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"x3 = {x3}")