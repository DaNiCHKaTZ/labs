def replace_last_occurrence(S, S1, S2):
    parts = S.rsplit(S1, 1)
    return S2.join(parts)

S = input("Введите строку S: ")
S1 = input("Введите строку S1: ")
S2 = input("Введите строку S2: ")

result = replace_last_occurrence(S, S1, S2)
print(result)
