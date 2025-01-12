import math
from functools import wraps

def cache_results(func):
    func.cache = {}

    @wraps(func)
    def wrapper(*args):
    
        key = tuple(tuple(arg) if isinstance(arg, list) else arg for arg in args)
        if key in func.cache:
            print(f'Результат для параметров {key} взят из кэша.')
            return func.cache[key]
        result = func(*args)
        func.cache[key] = result
        return result
    
    def print_cache():
        print('Кэшированные результаты:')
        for args, result in func.cache.items():
            print(f'Параметры: {args}, Результат: {result}')

    wrapper.print_cache = print_cache
    return wrapper

@cache_results
def calculate(numbers):
    arithmetic = sum(numbers) / len(numbers)
    geometric = math.prod(numbers) ** (1 / len(numbers))
    return arithmetic, geometric


result1 = calculate([1, 2, 3, 4, 5])
print(f'Результат 1: {result1}')

result2 = calculate([1, 2, 3, 4, 5]) 
print(f'Результат 2: {result2}')

result3 = calculate([2, 3, 4])
print(f'Результат 3: {result3}')


calculate.print_cache()
