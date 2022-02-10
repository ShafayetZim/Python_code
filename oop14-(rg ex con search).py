# Regular Expression
# more on search()

import re

pattern = r"color"
text = "Create color palettes with the color wheel or image, browse thousands of color"

match = re.search(pattern, text)

if match:
    print(match.start())  # start()-- returns starting index of the first match
    print(match.end())  # end()-- returns ending index
    print(match.span())  # span()-- returns both
