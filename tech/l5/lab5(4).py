import random

def inc_or_dec(seq):
    inc = all(x < y for x, y in zip(seq, seq[1:]))
    dec = all(x > y for x, y in zip(seq, seq[1:]))
    return inc or dec

def main():
    K = int(input("Введите количество наборов K: "))
    count_sets = 0

    input_method = input("Выберите способ ввода данных: ")

    for i in range(K):
        print(f"Введите элементы набора {i + 1}, завершите ввод числом 0:")
        seq = []
        if input_method == '1':
            while True:
                num = int(input())
                if num == 0:
                    break
                seq.append(num)
        elif input_method == '2':
            num_elements = random.randint(2, 10)  # Генерация случайного количества элементов (не менее двух)
            seq = [random.randint(-100, 100) for _ in range(num_elements)]
            print("Сгенерированный набор:", seq)
        else:
            print("Неверный выбор способа ввода данных.")
            return
        
        if len(seq) >= 2 and inc_or_dec(seq):
            count_sets += 1

    print("Количество наборов с возрастающими или убывающими элементами:", count_sets)

if __name__ == "__main__":
    main()
