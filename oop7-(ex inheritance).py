# inheritance exercise

class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("hi")

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
