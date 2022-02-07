# multiple inheritance

class Bird:
    def twitter(self):
        print("How birds sound!")

class Doyel():
    def twitter(self):
        print("chirp")

class Crow(Bird, Doyel):
    def twitter(self):
        print("Whistle")

sound = Crow()
sound.twitter()
