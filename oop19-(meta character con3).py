# meta character
# {from,to}$ means can match between the range
# cant match more than specified number

import re
pattern = r"a{1,3}$"


if re.match(pattern, "aaaa"):
    print("match")
else:
    print("not match")
