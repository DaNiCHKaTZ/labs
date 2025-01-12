 with open('C:\Users\user\Desktop\labs\case.txt', 'r') as file:
    array = [[21]  for _in range(21)]
    for i in range(21):
        line = file.readline().strip().split()  
        for j in range(21):
            array[i][j] = int(line[j])  

for row in array:
    print(row)