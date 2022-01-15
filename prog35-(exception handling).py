# Exception Handling

try:
    list = [10, 0, 30]
    result = list[0] / list[1]
    # result2 = list[0] / list[3] --> for index error
    print(result)
    print("done")

except ZeroDivisionError:
    print("divided by Zero is not possible")

except IndexError:
    print("index is out of bound")

print("exception handled")
