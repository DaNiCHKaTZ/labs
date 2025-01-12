def combine(N1, S1, N2, S2):
    return S1[:N1] + S2[-N2:]


N1 = int(input(" N1 = "),)
S1 = input("Введите первую строку ",)
N2 = int(input(" N2 = "),)
S2 = input("Введите вторую строку ",)
result = combine(N1, S1, N2, S2)
print(result)  
