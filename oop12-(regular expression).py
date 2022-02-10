# Regular Expression
# match() - it can matches only at the beginning of a string

import re

pattern = r"color"
if re.match(pattern, "Red is a color, I love red"):
    print("match")

else:
    print("not match")
