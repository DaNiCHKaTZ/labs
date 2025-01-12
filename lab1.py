import matplotlib.pyplot as plt
import numpy as np

def function1(phi):
    # Функция для первого графика
    return np.sin(phi)

def function2(phi):
    # Функция для второго графика
    return np.cos(phi)

def draw_image(phi1, phi2, delta_phi, R1, R2):
    # Создаем список для хранения точек пересечения каждого отрезка с графиком
    points1 = []
    points2 = []

    # Вычисляем количество шагов
    steps = int((phi2 - phi1) / delta_phi)

    # Вычисляем значения угла phi для каждого шага
    phi_values = np.linspace(phi1, phi2, steps)

    # Находим точки пересечения для каждого угла phi
    for phi in phi_values:
        x1 = R1 * np.cos(phi)
        y1 = R1 * np.sin(phi)
        points1.append((x1, y1))

        x2 = R2 * np.cos(phi)
        y2 = R2 * np.sin(phi)
        points2.append((x2, y2))

    # Создаем фигуру и оси
    fig, ax = plt.subplots()

    # Рисуем график первой функции
    ax.plot(phi_values, [function1(phi) for phi in phi_values], label='Function 1')

    # Рисуем график второй функции
    ax.plot(phi_values, [function2(phi) for phi in phi_values], label='Function 2')

    # Рисуем отрезки, соединяющие точки пересечения
    for i in range(len(points1)):
        x_values = [points1[i][0], points2[i][0]]
        y_values = [points1[i][1], points2[i][1]]
        ax.plot(x_values, y_values, color='red')

    # Рисуем окружности
    circle1 = plt.Circle((0, 0), R1, color='blue', fill=False)
    circle2 = plt.Circle((0, 0), R2, color='green', fill=False)
    ax.add_artist(circle1)
    ax.add_artist(circle2)

    # Добавляем легенду
    ax.legend()

    # Отображаем график
    plt.axis('equal')
    plt.show()

# Пример вызова функции
draw_image(0, np.pi*2, np.pi/16, 1, 2)