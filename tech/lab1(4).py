
with open('input.txt', 'r') as file:
    a = int(file.readline().strip())
    b = int(file.readline().strip())
    h = int(file.readline().strip())
    m = int(file.readline().strip())
    p = int(file.readline().strip())

S = 0.5 * (a + b) * h
t = (2 * m) / (p * S)


with open('lab1(4).txt', 'w') as f:
    f.write(str(t))

with open('lab1(4).txt', 'r') as f:
    content = f.read()

