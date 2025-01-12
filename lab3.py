import matplotlib.pyplot as plt

class BSplineCurve:
    def __init__(self, control_points, knots):
        self.control_points = control_points
        self.knots = knots

    def basis_function(self, i, k, t):
        if k == 0:
            return 1.0 if self.knots[i] <= t < self.knots[i+1] else 0.0

        denominator1 = self.knots[i+k] - self.knots[i]
        term1 = 0.0 if denominator1 == 0.0 else ((t - self.knots[i]) / denominator1) * self.basis_function(i, k-1, t)

        denominator2 = self.knots[i+k+1] - self.knots[i+1]
        term2 = 0.0 if denominator2 == 0.0 else ((self.knots[i+k+1] - t) / denominator2) * self.basis_function(i+1, k-1, t)

        return term1 + term2

    def evaluate(self, t):
        n = len(self.control_points) - 1
        p = 3

        if t < self.knots[p] or t > self.knots[n+1]:
            raise ValueError("Invalid parameter value")

        result = [0.0, 0.0]
        for i in range(n+1):
            basis = self.basis_function(i, p, t)
            result[0] += self.control_points[i][0] * basis
            result[1] += self.control_points[i][1] * basis

        return result

def onclick(event):
    if event.button == 1:
        control_points.append([event.xdata, event.ydata])
        plt.plot(event.xdata, event.ydata, 'ro')
        plt.draw()

def on_button_press(event):
    if event.key == 'enter':
        t_vals = [i/100 for i in range(101)]
        points = [curve.evaluate(t) for t in t_vals]
        x_coords, y_coords = zip(*points)
        plt.plot(x_coords, y_coords, 'b-')
        plt.draw()

# Инициализация пустого списка контрольных точек
control_points = []

# Отображение пустого графика
plt.figure()
plt.axis('equal')

# Привязка событий клика и кнопки
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.gcf().canvas.mpl_connect('key_press_event', on_button_press)

# Создание объекта кривой B-сплайнами
knots = [0, 0, 0, 0, 1, 2, 3, 3, 3, 3]
curve = BSplineCurve(control_points, knots)

# Отрисовка графика
plt.show()