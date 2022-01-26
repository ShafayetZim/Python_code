# method

class Student:
    roll = ""
    year = ""

    # constructor
    def __init__(self, roll, year):
        self.roll = roll
        self.year = year

    def display(self):
        print(f"Roll: {self.roll}, year: {self.year}")

mahi = Student(201, 2020)
mahi.display()

himi = Student(162, 2016)
himi.display()

