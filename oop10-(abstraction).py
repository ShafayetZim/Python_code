# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        area = .5 * self.base * self.height
        print("Triangle area: ", area)

class Rectangle(Shape):
    def area(self):
        area = self.base * self.height
        print("Rectangle area: ", area)

s = Triangle(10, 20)
s.area()
r = Rectangle(10, 20)
r.area()
