# inheritance

class Phone:
    def call(self):
        print("Calling is available")

    def message(self):
        print("Messaging is available")

# inherits the class attribute by giving name
class Samsung(Phone):
    def photo(self):
        print("Taking photo is available")

s = Samsung()
s.call()
s.message()
s.photo()

# checking if Samsung is a sub-class of Phone (super class)
print(issubclass(Samsung, Phone))
