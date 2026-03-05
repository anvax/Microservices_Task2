import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def compare_area(self, other):
        if not isinstance(other, Figure):
            return "Сравнивать можно только с фигурами"
        
        self_area = self.area()
        other_area = other.area()
        
        if self_area > other_area:
            return f"Площадь {self.__class__.__name__} больше, чем у {other.__class__.__name__}"
        elif self_area < other_area:
            return f"Площадь {self.__class__.__name__} меньше, чем у {other.__class__.__name__}"
        else:
            return "Площади фигур равны"

    def compare_perimeter(self, other):
        if not isinstance(other, Figure):
            return "Сравнивать можно только с фигурами"
        
        self_perim = self.perimeter()
        other_perim = other.perimeter()
        
        if self_perim > other_perim:
            return f"Периметр {self.__class__.__name__} больше, чем у {other.__class__.__name__}"
        elif self_perim < other_perim:
            return f"Периметр {self.__class__.__name__} меньше, чем у {other.__class__.__name__}"
        else:
            return "Периметры фигур равны"


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

rect = Rectangle(10, 20)
sq = Square(15)
circle = Circle(10)
tri = Triangle(3, 4, 5)

print(f"Площадь прямоугольника: {rect.area()}")
print(f"Площадь квадрата: {sq.area()}")
print(f"Периметр круга: {circle.perimeter():.2f}")
print(f"Площадь треугольника: {tri.area()}")
print(rect.compare_area(sq))
print(tri.compare_perimeter(sq))