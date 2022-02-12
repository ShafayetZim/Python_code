# Regular Expression
# sub() -- replaces pattern if find match
# count=! only replace the number specified from the first if find match

import re

pattern = r"color"
text = "Create color palettes with the color wheel or image, browse thousands of color"

match = re.sub(pattern, "paint", text)
match2 = re.sub(pattern, "paint", text, count=2)

print(match)
print(match2)

