# character class
# can match from a set of character
# can match only at the start
# for series have to maintain that pattern

import re
pattern = r"[aeiou]"
pattern2 = r"[A-Z]"
pattern3 = r"[0-9]"
pattern4 = r"[A-Z][a-z][0-9]"

if re.match(pattern4, "As9kk"):
    print("match")
else:
    print("not match")
