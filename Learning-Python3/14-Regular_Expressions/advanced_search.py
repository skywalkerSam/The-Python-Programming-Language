# Advanced Search...

import re

"""
- https://regex101.com/

"""

a_note = "This is an odinary note. Please don't search in here! - No search results ;("

pattern = re.compile(r"[a-zA-Z].([e])")

a = pattern.search(a_note)
b = pattern.match(a_note)
c = pattern.fullmatch(a_note)
d = pattern.findall(a_note)

print(a)
print(b)
print(c)
print(d)





