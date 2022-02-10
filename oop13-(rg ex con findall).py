# Regular Expression
# search() - it can matches anywhere of a string
# findall() - it can matches anywhere of a string and returns a list of substring that matches

import re

pattern = r"color"

# search()
if re.search(pattern, "Red is a color, I love red"):
    print("match")

else:
    print("not match")

# findall()
print(re.findall(pattern, "Red is a color, I love red color"))
