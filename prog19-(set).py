# set
num1 = {1, 2, 3, 4}
num2 = set([4, 5, 6])

num2.add(7)
num1.remove(2)

print("Set1: ", num1)
print("Set1: ", num2)
print(2 in num1)  # check 2 is in the list1 after removing
print(7 in num2)  # check 7 is in the list2 after adding

# union (sign = '|')
print(num1 | num2)

# intersection (sign = '&')
print(num1 & num2)

# difference (sign = '-')
print(num1 - num2)
