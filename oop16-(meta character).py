# meta character
# (.) dot matches any character
# (^) matches from the simple to dot
# ($) matches after dot to end

import re
pattern1 = "col..r"
pattern2 = "^col..r"
pattern3 = "col..r$"
pattern4 = "^col..r$"

if re.match(pattern2, "colour"):
    print("match")
else:
    print("not match")
