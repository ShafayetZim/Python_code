# stack
books = []

# push
books.append("Python")
books.append("Java")
books.append("Php")
print(books)

# pop
books.pop()
print("Now the top book is: ", books[-1])

books.pop()
print("Now the top book is: ", books[-1])

books.pop()

# Checking empty
if not books:
    print("No books left.")

