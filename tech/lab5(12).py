M = int(input("Введите количество строк (M): "))
N = int(input("Введите количество столбцов (N): "))
K = int(input("Введите номер строки (K): "))

if 1 <= K <= M:

    matrix = []
    for i in range(M):
        row = list(map(int, input(f"Введите элементы {i + 1}-й строки через пробел: ").split()))
        matrix.append(row)
    
    
    print(f"Элементы {K}-й строки:", matrix[K - 1])
else:
    print("Неверное значение K. Оно должно быть в диапазоне от 1 до M.")
