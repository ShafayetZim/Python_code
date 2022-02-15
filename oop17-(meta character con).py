# meta character
# * matches indefinite number
# * means Zero(0) or more
# + means One(1) or more

import re
pattern = r"a*"
pattern2 = r"(ab)*"
pattern3 = r"a+"
pattern4 = r"a+b"  # it means after a have to exist one or more b


if re.match(pattern4, "aaabcolour"):
    print("match")
else:
    print("not match")
