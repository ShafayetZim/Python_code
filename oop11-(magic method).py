# magic method

class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # this is a magic method
    def __str__(self):
        return (f"Name = {self.name}, Color = {self.color}")

    # equality check using magic method
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    # def display(self):
    #     print(f"Name = {self.name}, Color = {self.color}")

bike1 = Bike("Yamaha R15", "Blue")
bike2 = Bike("Yamaha FZ", "Red")
bike3 = Bike("Yamaha FZ", "Red")

print(bike1)
print(bike2 == bike3)
