def check_string(s):

    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return 1
  
    try:
        float(s)
        return 2
    except ValueError:
        return 0

s = input("Введите строку ",)
result = check_string(s)
print(result)
