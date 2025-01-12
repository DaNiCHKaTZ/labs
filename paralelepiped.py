import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

def delaunay(points):
    points = np.asarray(points, dtype=np.float64)

    if points.ndim != 2:
        raise ValueError("Input points must be 2-D.")

    ndim = points.shape[1]

    if ndim > 3:
        raise ValueError("Delaunay triangulation only supports 2-D or 3-D input points.")

    if points.size == 0:
        raise ValueError("Input points must not be empty.")

    if points.size <= ndim:
        raise ValueError("Input points must have at least (ndim+1) unique points.")

    if ndim == 2:
        qhull_options = "Qt"
    else:
        qhull_options = "Qbb Qc Qz"

    from scipy.spatial.qhull import _qhull, QhullError, _QhullUser

    try:
        if points.flags.c_contiguous:
            points = np.ascontiguousarray(points, dtype=np.double)
            data = _qhull.delaunay(points, qhull_options)
        else:
            data = _qhull.delaunay(points.copy(order='C'), qhull_options)
    except QhullError as e:
        raise ValueError(str(e))

    return delaunay(points, data)

# Создание пустого списка для хранения контрольных точек
control_points = []

# Обработчик события клика мыши
def on_click(event):
    # Если кнопка мыши нажата
    if event.button == 1:
        # Получаем координаты клика
        x, y = event.xdata, event.ydata
        # Добавляем точку в список контрольных точек
        control_points.append([x, y])
        # Рисуем точку на графике
        plt.plot(x, y, 'ro')
        plt.draw()

# Создание графического окна и настройка обработчика событий
fig, ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', on_click)

# Отображение графического окна
plt.show()

# Конвертация списка контрольных точек в массив numpy
control_points = np.array(control_points)

# Построение выпуклой оболочки путем алгоритма триангуляции Делоне
tri = Delaunay(control_points)

# Отображение триангуляции на графике
plt.triplot(control_points[:,0], control_points[:,1], tri.simplices)
plt.plot(control_points[:,0], control_points[:,1], 'ro')
plt.show()
