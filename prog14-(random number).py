# guessing game
# random number

from random import randint

for x in range(1, 6):
    guessNumber = int(input("Enter your guessing number(1-5):"))
    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print("You guessed right")

    else:
        print("You guessed wrong.")
        print("Random number was:", randomNumber)

