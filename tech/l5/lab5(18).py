from itertools import combinations
from math import sqrt
import random

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def perimeter(triangle):
    return distance(triangle[0], triangle[1]) + distance(triangle[1], triangle[2]) + distance(triangle[2], triangle[0])

def max_perimeter(points):
    max_perimeter = 0
    best_triangle = None
    for triangle in combinations(points, 3):
        buff_perimeter = perimeter(triangle)
        if buff_perimeter > max_perimeter:
            max_perimeter = buff_perimeter
            best_triangle = triangle
    return best_triangle, max_perimeter

choice = input("Выберите способ ввода данных : ")

if choice == '1':
    N = int(input("Введите количество точек: "))
    points = []
    for _ in range(N):
        x, y = map(int, input("Введите координаты точки (x y): ").split())
        points.append((x, y))
elif choice == '2':
    N = int(input("Введите количество точек: "))
    points = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(N)]
    print("Сгенерированные точки:", points)
else:
    print("Неверный выбор!")
    points = []

if len(points) >= 3:
    best_triangle, max_perimeter = max_perimeter(points)
    print("Наибольший периметр:", max_perimeter)
    print("Точки треугольника:", best_triangle)
else:
    print("Недостаточно точек для формирования треугольника.")
