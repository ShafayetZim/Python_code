# exercise oop

class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate(self):
        area = .5 * self.base * self.height
        print("Area: ", area)

kitchen = Triangle(10, 20)
kitchen.calculate()
dining = Triangle(15, 25)
dining.calculate()
