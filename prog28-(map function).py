# map function
def square(x):
    return x*x

num = [1, 2, 3, 4]
result = list(map(square, num))
print(result)
