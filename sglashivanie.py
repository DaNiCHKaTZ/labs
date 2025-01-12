import tkinter as tk

# Создание окна
window = tk.Tk()
window.title("Сглаживание изображения")

# Холст для отрисовки
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Список для хранения координат отрезков
lines = []

# Переменная для хранения состояния галочки
smoothing_enabled = tk.BooleanVar()
smoothing_enabled.set(False)
 
# Функция для отрисовки отрезков
def draw_lines(event):
    x = event.x
    y = event.y
    lines.append((x, y))
    if len(lines) > 1:
        # Отрисовка линии между последними двумя точками
        x1, y1 = lines[-2]
        x2, y2 = lines[-1]
        if smoothing_enabled.get():
            # Сглаживание с использованием увеличения частоты выборки
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            steps = max(dx, dy)
            x_step = (x2 - x1) / steps
            y_step = (y2 - y1) / steps
            for i in range(steps):
                x = x1 + i * x_step
                y = y1 + i * y_step
                canvas.create_oval(x, y, x+1, y+1, fill="black")
        else:
            canvas.create_line(x1, y1, x2, y2, fill="black")

# Привязка функции к событию "нажатие мыши"
canvas.bind("<Button-1>", draw_lines)

# Создание галочки для включения сглаживания
checkbox = tk.Checkbutton(window, text="Сглаживание", variable=smoothing_enabled)
checkbox.pack()

# Запуск главного цикла окна
window.mainloop()