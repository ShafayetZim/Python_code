# find max num

num1 = 30
num2 = 20
num3 = 40

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)

if num2 > num1:           # you can use else
    if num2 > num3:
        print(num2)
    else:
        print(num3)