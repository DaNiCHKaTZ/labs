def sum():
    current_sum = 0
    for n in range(100):
        current_sum += 1 / (3 ** (2 * n))
        yield current_sum


for sum_value in sum():
    print(sum_value)
