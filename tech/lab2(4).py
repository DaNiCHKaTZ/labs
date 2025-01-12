a=int(input("Введите a "))
hun = (a // 100) % 10
ten = (a // 10) % 10
num = a % 10


match hun:
    case 1:
        print("Сто ")
    case 2:
        print("Двесте ")
    case 3:
        print("Триста ")
    case 4:
        print("Четыреста ")
    case 5 :
        print("Пятьсот ")
    case 6:
        print("Шестьсот ")
    case 7:
        print("Семсот" )
    case 8:
        print("Восемсот ")
    case 9:
        print("Девятьсот")

match ten:
    case 0:
        print("")
    case 1:
        print("Десять ")
    case 2:
        print("Двадцать ")
    case 3:
        print("Тридцать ")
    case 4:
        print("Сорок ")
    case 5:
        print("Пятьдесят ")
    case 6:
        print("Шестьдесят ")
    case 7:
        print("Семдесят" )
    case 8:
        print("Восемдесят ")
    case 9:
        print("Девяносто")


match num:
    case 0:
        print("")
    case 1:
        print("один ")
    case 2:
        print("два ")
    case 3:
        print("три ")
    case 4:
        print("четыре ")
    case 5:
        print("пять ")
    case 6:
        print("Шесть ")
    case 7:
        print("Семь" )
    case 8:
        print("Восем ")
    case 9:
        print("Девять")