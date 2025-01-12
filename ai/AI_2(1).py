import numpy as np

def norm(data, m):
    m[0] = min(min(row) for row in data)
    m[1] = max(max(row) for row in data)
    for i in range(len(data)):
        newData = [(data[i][j] - m[0]) / (m[1] - m[0]) for j in range(len(data[i]))]
        data[i] = tuple(newData)

def unNorm(data, m):
    return data * (m[1] - m[0]) + m[0]

def f(x):
    return np.tanh(x)

def df(x):
    return 1 - np.tanh(x) ** 2

W1 = np.random.rand(3, 10)  
W2 = np.random.rand(10)    

def go_forward(inp):
    sum = np.dot(inp, W1)
    out = np.tanh(sum)
    sum = np.dot(out, W2)
    y = np.tanh(sum)
    return y, out

def train(epoch):
    global W2, W1
    lmd = 0.01  
    N = 500000  
    count = len(epoch)
    for k in range(N):
        x = epoch[np.random.randint(0, count)]
        y, out = go_forward(x[0:3])
        e = y - x[-1]
        localGrad = e * df(y)

        W2 -= lmd * localGrad * out

        localGrad2 = W2 * localGrad * df(out)
        W1 -= lmd * np.outer(x[0:3], localGrad2)

data = [80, 79, 85, 80, 75, 68, 65, 68, 65, 62]

epoch = [(data[i], data[i+1], data[i+2], data[i+3]) for i in range(len(data) - 3)]

m = [0, 0]
norm(epoch, m)

train(epoch)

print("")
sum = 0
for x in epoch:
    y, out = go_forward(x[0:3])
    y = unNorm(y, m)
    y0 = unNorm(x[-1], m)
    sum += (y - y0) ** 2
    print(f"Проверка значений НС: {y} => {y0}")

predict = [(data[7], data[8], data[9])]
norm(predict, m)
y, out = go_forward(predict[0])
y = unNorm(y, m)
print(f"Стоимость в следующем году: {y}")
