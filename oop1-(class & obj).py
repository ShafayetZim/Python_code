# class & object

class Student:
    roll = ""
    year = ""

# object creation
mahi = Student()

# checking if object creation is working properly
print(isinstance(mahi, Student))

# using class property by object & dot (.) operator
mahi.roll = 101
mahi.year = 2020

print(f"Roll: {mahi.roll}, year: {mahi.year}")
