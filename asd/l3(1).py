def find_max_profit(prices):
    if len(prices) < 2:
        return None
    
    # Рекурсивная функция для поиска максимальной прибыли
    def find_max_profit_helper(prices, left, right):
        # Базовый случай - если длина массива равна 2, возвращаем прибыль
        if right - left == 1:
            return left, right, prices[right] - prices[left]
        
        mid = (left + right) // 2
        
        # Рекурсивно находим максимальную прибыль для левой и правой половин массива
        left_start, left_end, left_profit = find_max_profit_helper(prices, left, mid)
        right_start, right_end, right_profit = find_max_profit_helper(prices, mid, right)
        
        # Находим максимальную прибыль для пересечения левой и правой половин массива
        cross_start = cross_end = mid
        while cross_start >= left and prices[mid] - prices[cross_start] >= 0:
            cross_start -= 1
        while cross_end <= right and prices[cross_end] - prices[mid] >= 0:
            cross_end += 1
        cross_profit = prices[cross_end - 1] - prices[cross_start + 1]
        
        # Возвращаем максимальную прибыль из трех вариантов
        if left_profit >= cross_profit and left_profit >= right_profit:
            return left_start, left_end, left_profit
        elif cross_profit >= left_profit and cross_profit >= right_profit:
            return cross_start + 1, cross_end - 1, cross_profit
        else:
            return right_start, right_end, right_profit
    
    # Вызываем рекурсивную функцию для всего массива
    return find_max_profit_helper(prices, 0, len(prices) - 1)


prices = [6, 5, 4, 3, 2, 10, 8, 7, 9]
start, end, profit = find_max_profit(prices)
print("День покупки:", start+1)
print("День продажи:", end+1)
print("Полученная прибыль:", profit)