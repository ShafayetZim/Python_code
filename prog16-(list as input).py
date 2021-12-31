numberOfWords = 0
numberOfLetters = 0
numberOfDigits = 0

text = input("Enter a number of inputs: ")

for x in text:
    # makes lower if found uppercase
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numberOfLetters = numberOfLetters + 1

    if x >= '0' and x <= '9':
        numberOfDigits = numberOfDigits + 1

# if space found count ia as a word
    if x == ' ':
        numberOfWords = numberOfWords + 1

print("Letters: ", numberOfLetters)
print("Digits: ", numberOfDigits)
# add 1 because word number is always 1 higher than spaces
print("Words: ", numberOfWords + 1)
