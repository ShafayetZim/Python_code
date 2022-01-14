# file read

file = open("text.txt", "r")  # "r" for read
# "w" for write, "r+" for both
# print(file.readable())

a = file.read()
print(a)

# b = file.readlines()
# print(b)

# using index
# c = file.readlines()[0]
# print(c)

# using for loop
# for line in file:
#     print(line)

file.close()
