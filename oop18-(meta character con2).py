# meta character
# ? means Zero(0) or One(1)
# cant match more than 1

import re
pattern = r"ice(-)?cream"


if re.match(pattern, "ice-cream"):
    print("match")
else:
    print("not match")
