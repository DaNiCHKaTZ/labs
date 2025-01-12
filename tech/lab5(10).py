def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def perimeter(triangle):
    return (distance(triangle[0], triangle[1]) +
            distance(triangle[1], triangle[2]) +
            distance(triangle[2], triangle[0]))


N = int(input("Введите количество точек: "))


points = [tuple(map(int, input(f"Введите координаты точки {i + 1}").split())) for i in range(N)]


max_perimeter = 0
best_triangle = None

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            triangle = (points[i], points[j], points[k])
            current_perimeter = perimeter(triangle)
            if current_perimeter > max_perimeter:
                max_perimeter = current_perimeter
                best_triangle = triangle


if best_triangle:
    print("Наибольший периметр:", max_perimeter)
    print("Точки треугольника с наибольшим периметром:", best_triangle)
else:
    print("Не удалось найти треугольник.")
