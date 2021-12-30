# split

n = input("Enter a text of input:")
# ex 10 20 30...
list = n.split()
# splits like 10, 20, 30

sum = 0
for num in list:
    sum = sum + int(num)
    # num is string so make it int

print(sum)
