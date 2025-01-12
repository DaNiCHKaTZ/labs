def replace(s):
    words = s.split()
    result = '.'.join(words)
    return result


s = input("Введите стрку ", )
result = replace(s)
print(result)
