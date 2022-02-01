# method overriding

class Animal:
    def __init__(self):
        print("Barking")

class Cat(Animal):
    def __init__(self):  # this overrides method
        print("Mew")

class Dog(Animal):
    def __init__(self):
        # accessing parent class
        super().__init__()
        print("baw-waw")

c = Cat()
d = Dog()
