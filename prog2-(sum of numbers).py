num1 = input("Enter 1st Number:")
num2 = input("Enter 2nd Number:")

# without type casting
sum1 = num1 + num2

# type casting
sum2 = int(num1) + int(num2)
sum3 = float(num1) + float(num2)

print("ans:", sum1)  # returns string
print("ans:", sum2)
print("ans:", sum3)
