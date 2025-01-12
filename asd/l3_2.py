from min_price import *
from find_min_price import *
items = {}
sets = {}
needed_items = []
def find_min_price(items, sets, needed_items):
    min_prices = {}
    min_prices[()] = 0

    for i in range(1, len(needed_items) + 1):
        min_prices[(needed_items[i-1],)] = float('inf')

        for j in range(1, i + 1):
            for set_items, set_price in sets.items():
                if tuple(needed_items[i-j:i]) in set_items:
                    min_price = min_prices[tuple(needed_items[i-j:i])] + set_price
                    if min_price < min_prices[(needed_items[i-1],)]:
                        min_prices[(needed_items[i-1],)] = min_price

    return min_prices[(needed_items[-1],)]




num_items = int(input("Введите количество товаров: "))
for _ in range(num_items):
    item_name = input("Введите название товара: ")
    item_price = float(input("Введите цену товара: "))
    items[item_name] = item_price

num_sets = int(input("Введите количество наборов товаров: "))
for _ in range(num_sets):
    set_name = input("Введите название набора товаров: ")
    set_items = input("Введите набор товаров через запятую: ").split(",")
    set_price = float(input("Введите цену набора товаров: "))
    sets[tuple(set_items)] = set_price

needed_items = input("Введите нужные товары через запятую: ").split(",")

# Вычисляем минимальную цену и определяем, можно ли ее достичь наборами
min_price = find_min_price(items, sets, needed_items)
can_reach = min_price != float('inf')
displayText()
#dissplayText()
#print("Наименьшая цена: ", min_price)
#print("Можно достичь наборами: ", can_reach)
