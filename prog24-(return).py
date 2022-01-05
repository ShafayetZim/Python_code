#add number
def add(a, b):
    sum = a + b
    return sum
result = add(10,20)
print("sum:", result)

#find max
def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(20,40))

# assign a function to a variable
maximum = max
print(maximum(50, 10))
