# multi-level inheritance

class Bird:
    def twitter1(self):
        print("How birds sound!")

class Doyel(Bird):
    def twitter2(self):
        print("chirp")

class Crow(Doyel):
    def twitter3(self):
        print("Whistle")

sound = Crow()
sound.twitter1()
sound.twitter2()
sound.twitter3()