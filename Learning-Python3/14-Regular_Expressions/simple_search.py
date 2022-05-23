from ast import pattern
import re

string = "Search me! This is a string..."

print("me" in string)


#2
print(re.search("This", string))    # It returns an object.
print(re.search("this", string))

a = re.search("me", string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())


#3
a_note = "This is an odinary note. Please don't search in here! - No search results ;("
pattern = re.compile("search")

a = pattern.search(a_note)
b = pattern.match(a_note)
c = pattern.fullmatch(a_note)
d = pattern.findall(a_note)

print(a)
print(b)
print(c)
print(d)










