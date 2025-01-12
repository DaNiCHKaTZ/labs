def find_min_price(prices):
    n = len(prices)
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    combinations = [[[] for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 0
    
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j]
            combinations[i][j] = combinations[i-1][j]
            
            if dp[i][j-1] + sum(prices[i-1]) < dp[i][j]:
                dp[i][j] = dp[i][j-1] + sum(prices[i-1])
                combinations[i][j] = combinations[i-1][j-1] + [i]
    
    min_price = float('inf')
    min_combinations = []
    
    for j in range(1, n+1):
        if dp[n][j] < min_price:
            min_price = dp[n][j]
            min_combinations = combinations[n][j]
    
    return min_price, min_combinations

n = int(input("Введите количество товаров: "))
prices = []
for i in range(n):
    price = list(map(int, input(f"Введите цены товаров в {i+1} наборе, через пробел: ").split()))
    prices.append(price)

min_price, min_combinations = find_min_price(prices)

print("Наименьшая цена:", min_price)
print("Наборы товаров со скидками:", min_combinations)