import matplotlib.pyplot as plt
import numpy as np

# Создаем списки для хранения координат x и y контрольных точек
control_points_x = []
control_points_y = []

# Создаем функцию-обработчик события клика
def onclick(event):
    # добавляем в конец списка точки
    control_points_x.append(event.xdata)
    control_points_y.append(event.ydata)

    # После добавления новой точки перерисовываем график
    draw()

# Создаем функцию для отрисовки кривой Безье
def draw_bezier_curve(control_points_x, control_points_y):
    # Если есть контрольные точки, отрисовываем кривую Безье
    if len(control_points_x) > 1:
        t = np.linspace(0, 1, 100)  # Создаем массив значений параметра t от 0 до 1
        n = len(control_points_x) - 1  # Определяем степень кривой Безье

        # Инициализируем массивы для хранения координат x и y кривой Безье
        bezier_curve_x = np.zeros_like(t)
        bezier_curve_y = np.zeros_like(t)

        # Вычисляем координаты кривой Безье в каждой точке t
        for i in range(n + 1):
            bezier_curve_x += control_points_x[i] * binomial_coefficient(n, i) * (1 - t)**(n - i) * t**i
            bezier_curve_y += control_points_y[i] * binomial_coefficient(n, i) * (1 - t)**(n - i) * t**i

        plt.plot(bezier_curve_x, bezier_curve_y, 'r-')  # Отрисовываем кривую Безье

# Функция для вычисления биномиального коэффициента
def binomial_coefficient(n, k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))

# Создаем функцию для отрисовки графика с контрольными точками и кривой Безье
def draw():
    plt.clf()  # Очищаем предыдущий график

    # Если есть контрольные точки, отрисовываем их
    if control_points_x and control_points_y:
        plt.scatter(control_points_x, control_points_y, c='b')  # Отрисовываем контрольные точки

        draw_bezier_curve(control_points_x, control_points_y)  # Отрисовываем кривую Безье 
    plt.gca().set_aspect('equal', adjustable='box')  # Устанавливаем соотношение сторон

    plt.show()  # Отображаем график

# Создаем график
fig, ax = plt.subplots()
plt.title('Bezier Curve')
plt.xlabel('X')
plt.ylabel('Y')

# Привязываем функцию-обработчик к событию клика
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Запускаем основной цикл программы
plt.show()