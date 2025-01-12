import tkinter as tk
from tkinter import messagebox, filedialog

class IcosahedronApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Царенко Д. Д. 10 Вариант")

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Сохранить...", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.root.quit)

        results_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Результаты", menu=results_menu)
        results_menu.add_command(label="Показать", command=self.show_results)

        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="Условие задачи", command=self.show_task)
        help_menu.add_command(label="О программе", command=self.show_about)

    def create_widgets(self):
        tk.Label(self.root, text="Число рёбер в каждой грани:").grid(row=0, column=0, padx=10, pady=5)
        self.edges_per_face = tk.Entry(self.root)
        self.edges_per_face.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Число рёбер, сходящихся в каждой вершине:").grid(row=1, column=0, padx=10, pady=5)
        self.edges_per_vertex = tk.Entry(self.root)
        self.edges_per_vertex.grid(row=1, column=1, padx=10, pady=5)

        self.calc_volume = tk.BooleanVar()
        tk.Checkbutton(self.root, text="Вычислить объём", variable=self.calc_volume).grid(row=2, column=0, padx=10, pady=5)

        self.calc_surface_area = tk.BooleanVar()
        tk.Checkbutton(self.root, text="Вычислить площадь поверхности", variable=self.calc_surface_area).grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Рассчитать", command=self.calculate).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.status = tk.Label(self.root, text="Готово", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write("Результаты вычислений:\n")
                file.write(f"Число рёбер в каждой грани: {self.edges_per_face.get()}\n")
                file.write(f"Число рёбер, сходящихся в каждой вершине: {self.edges_per_vertex.get()}\n")
                if self.calc_volume.get():
                    file.write(f"Объём: {self.volume}\n")
                if self.calc_surface_area.get():
                    file.write(f"Площадь поверхности: {self.surface_area}\n")
            self.status.config(text="Файл сохранён")

    def show_results(self):
        results = f"Число рёбер в каждой грани: {self.edges_per_face.get()}\n"
        results += f"Число рёбер, сходящихся в каждой вершине: {self.edges_per_vertex.get()}\n"
        if self.calc_volume.get():
            results += f"Объём: {self.volume}\n"
        if self.calc_surface_area.get():
            results += f"Площадь поверхности: {self.surface_area}\n"
        messagebox.showinfo("Результаты", results)

    def show_task(self):
        task_text = "Приложение для расчёта параметров икосаэдра. Введите значения числа рёбер в каждой грани и числа рёбер, сходящихся в каждой вершине. Выберите вычисления объёма и площади поверхности икосаэдра."
        messagebox.showinfo("Условие задачи", task_text)

    def show_about(self):
        about_text = "Приложение для расчёта параметров икосаэдра. Разработчик: Царенко Д. Д."
        messagebox.showinfo("О программе", about_text)

    def calculate(self):
        try:
            edges_per_face = int(self.edges_per_face.get())
            if edges_per_face <= 0:
                raise ValueError("Число рёбер в каждой грани должно быть положительным")
                
            edges_per_vertex = int(self.edges_per_vertex.get())
            if edges_per_vertex <= 0:
                raise ValueError("Число рёбер, сходящихся в каждой вершине, должно быть положительным")
                
            self.volume = (5 * (3 + (5 ** 0.5)) / 12) * (edges_per_face ** 3)
            self.surface_area = 5 * (3 ** 0.5) * (edges_per_face ** 2)
            self.status.config(text="Вычисления завершены")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")
            self.status.config(text="Ошибка ввода")

if __name__ == "__main__":
    root = tk.Tk()
    app = IcosahedronApp(root)
    root.mainloop()
