def step_function(x):
    return 1 if x >= 0 else 0

def xor(x1, x2):

    w11, w12 = 1, 1
    w21, w22 = 1, 1
    w31, w32 = -1, 1
    

    y1 = step_function(x1 * w11 + x2 * w12 - 1.5) 
    y2 = step_function(x1 * w21 + x2 * w22 - 0.5) 
    y = step_function(y1 * w31 + y2 * w32 - 0.5)  
    
    return y
print("")
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

for x1, x2 in inputs:
    print(f"XOR({x1}, {x2}) = {xor(x1, x2)}")
