# **args
# allows to pass arguments with their name

def student(**details):
    print(details)
    print(details["name"])

student(id=101, name="zim")