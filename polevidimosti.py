from tkinter import *

# Класс, представляющий стрелку
class Arrow:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.canvas = canvas
        self.line = canvas.create_line(x1, y1, x2-10, y2, fill="blue", width=15)
        self.head = canvas.create_polygon([x2, y2, x2 - 40, y2 - 30, x2 - 40, y2 + 30], fill="blue")

    # Проверка видимости стрелки по полю отсечения
    def is_visible(self, x1, y1, x2, y2):
        if (self.intersect(x1, y1, x2, y1, x2, y2) or
            self.intersect(x1, y1, x1, y2, x2, y2) or
            self.intersect(x1, y2, x2, y2, x2, y1) or
            self.intersect(x2, y1, x2, y2, x1, y2)):
            return False
        return True

    # Проверка пересечения линии с отрезком (ax, ay) -> (bx, by)
    def intersect(self, x1, y1, x2, y2, ax, ay):
        # Проверка положения точки относительно линии
        def orientation(x1, y1, x2, y2, px, py):
            return (y2 - y1) * (px - x2) - (x2 - x1) * (py - y2)

        if (orientation(x1, y1, x2, y2, ax, ay) == 0 and
            min(x1, x2) <= ax <= max(x1, x2) and
            min(y1, y2) <= ay <= max(y1, y2)):
            return True
        return False

    # Перемещение точки стрелки
    def move(self, dx, dy):
        self.canvas.move(self.line, dx, dy)
        self.canvas.move(self.head, dx, dy)

# Класс, представляющий окно приложения
class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=400, height=400, bg="white")
        self.canvas.pack()
        self.arrow = None

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    # Обработчик события клика мыши
    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    # Обработчик события перемещения мыши при зажатой кнопке
    def on_drag(self, event):
        if self.arrow:
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            self.arrow.move(dx, dy)
            self.start_x = event.x
            self.start_y = event.y

    # Обработчик события отпускания кнопки мыши
    def on_release(self, event):
        if not self.arrow:
            x1, y1 = self.start_x, self.start_y
            x2, y2 = event.x, event.y
            self.arrow = Arrow(self.canvas, x1, y1, x2, y2)
        else:
            self.canvas.delete(self.arrow.line)
            self.canvas.delete(self.arrow.head)
            self.arrow = None

# Создание и запуск приложения
root = Tk()
app = App(root)
root.mainloop()