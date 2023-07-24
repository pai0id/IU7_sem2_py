import tkinter as tk
from itertools import combinations


# Функция для нахождения биссектрисы треугольника
def find_bisector(p1, p2, p3):
    # Вычисление длин сторон треугольника
    a = ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** 0.5
    b = ((p3[1] - p1[1]) ** 2 + (p3[0] - p1[0]) ** 2) ** 0.5
    c = ((p3[1] - p2[1]) ** 2 + (p3[0] - p2[0]) ** 2) ** 0.5

    if b * c != 0:
        # Вычисление косинуса угла beta с использованием теоремы косинусов
        cos_beta = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    else:
        cos_beta = 0

    # Вычисление синуса угла beta
    sin_beta = (1 - cos_beta ** 2) ** 0.5

    # Вычисление координат точки на биссектрисе
    x = p1[0] + b * cos_beta
    y = p1[1] + b * sin_beta

    return x, y


# Класс, представляющий треугольник
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    # Разделение треугольника
    def split_triangle(self):
        bisector1 = find_bisector(self.p1, self.p2, self.p3)
        bisector2 = find_bisector(self.p2, self.p1, self.p3)
        t1 = Triangle(self.p1, bisector1, bisector2)
        t2 = Triangle(self.p2, bisector1, bisector2)
        t3 = Triangle(self.p3, bisector1, bisector2)
        return t1, t2, t3

    # Вычисление площади треугольника
    def area(self):
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2


# Класс, представляющий приложение для рисования треугольников
class TriangleApp:
    def __init__(self, master):
        self.master = master
        self.triangles = []
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.add_point)
        self.canvas.bind('<Button-3>', self.clear_points)
        self.button = tk.Button(master, text='Find triangle', command=self.find_triangle)
        self.button.pack()

    # Добавление точки на холст при щелчке левой кнопкой мыши
    def add_point(self, event):
        self.canvas.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill='black')
        self.triangles.append((event.x, event.y))

    # Очистка холста при щелчке правой кнопкой мыши
    def clear_points(self, event):
        self.canvas.delete('all')
        self.triangles.clear()

    # Поиск треугольника с наименьшей разностью площадей
    def find_triangle(self):
        if len(self.triangles) >= 3:
            min_diff = float('inf')
            min_triangle = None
            for t in combinations(self.triangles, 3):
                triangle = Triangle(*t)
                t1, t2, t3 = triangle.split_triangle()
                diff = abs(t1.area() - t2.area()) + abs(t1.area() - t3.area()) + abs(t2.area() - t3.area())
                if diff < min_diff:
                    min_diff = diff
                    min_triangle = triangle

            if min_triangle is not None:
                self.canvas.delete('result')
                self.canvas.create_polygon(*min_triangle.p1, *min_triangle.p2, *min_triangle.p3, outline='red', width=2,
                                           tags='result')
