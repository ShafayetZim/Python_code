# *args
def student(*details):
    print(details)

student(101, "zim")
student(102, "sakib", 4)

# it allows passing variable with no arguments
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(10, 20)
add(2, 3, 4)
