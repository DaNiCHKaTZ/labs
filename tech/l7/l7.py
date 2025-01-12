import math

class CETriangle:
    def __init__(self, name, x):
        self.__name = name
        self.__x = x

    def name(self):
        return self.__name

    def x(self):
        return self.__x

    def perimeter(self):
        return 3 * self.__x

    def area(self):
        return (math.sqrt(3) / 4) * (self.__x ** 2)

    def display(self):
        print(f"Название: {self.__name}")
        print(f"Длина стороны: {self.__x}")
        print(f"Периметр: {self.perimeter()}")
        print(f"Площадь: {self.area()}")

class CRTPrism(CETriangle):
    def __init__(self, name, x, h):
        super().__init__(name, x)
        self.__h = h

    @property
    def h(self):
        return self.__h

    def volume(self):
        return self.area() * self.__h

    def area(self):
        base_area = super().area()
        lateral_area = self.perimeter() * self.__h
        return 2 * base_area + lateral_area

    def display(self):
        super().display()
        print(f"Высота: {self.__h}")
        print(f"Объем: {self.volume()}")

def main():
    triangles = [
        CETriangle("Треугольник 1", 3),
        CETriangle("Треугольник 2", 4),
        CETriangle("Треугольник 3", 5)
    ]

    print("Треугольники:")
    for triangle in triangles:
        triangle.display()
        print()

    sum_area = sum(triangle.area() for triangle in triangles)
    sred_s = sum_area / len(triangles)

    s_below = [triangle for triangle in triangles if triangle.area() < sred_s]
    print(sred_s)
    print(f"Количество треугольников с площадью меньше средней: {len(s_below)}\n")

    prisms = [
        CRTPrism("Призма 1", 3, 6),
        CRTPrism("Призма 2", 4, 5),
        CRTPrism("Призма 3", 5, 4)
    ]

    print("Призмы:")
    for prism in prisms:
        prism.display()
        print()

    max_v = max(prisms, key=lambda prism: prism.volume())
    print("Призма с наибольшим объемом:")
    max_v.display()

if __name__ == "__main__":
    main()
