a = int(input("Введите четырехзначное число: "))

if a > 9999 or a < 1000:
    print("Число не четырехзначное")
else:
    th = a // 1000
    hun = (a // 100) % 10
    ten = (a // 10) % 10
    num = a % 10
    
    
    new_number = th * 1000 + ten * 100 + hun * 10 + num
    
    print("Новое число:", new_number)