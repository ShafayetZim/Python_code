# method

class Student:
    roll = ""
    year = ""

    def set_value(self, roll, year):
        self.roll = roll
        self.year = year

    def display(self):
        print(f"Roll: {self.roll}, year: {self.year}")

# using method set_value
mahi = Student()
mahi.set_value(201, 2020)
mahi.display()

# using . operator
himi = Student()
himi.roll = 162
himi.year = 2016
himi.display()



