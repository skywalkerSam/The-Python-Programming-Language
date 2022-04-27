
"""
Developer: Mr. Skywalker
Purpose: Human Program
Stardate: 12021.242.01:21:00

"""


class Human():
    def __init__(self, mindset="\nScientist\n", nature="Creator\n", work="Explorer\n", thinking="Dreamer\n"):
        self.mindset = mindset
        self.nature = nature
        self.work = work
        self.thinking = thinking

    def Intro(self):
        return ">_  Hello, I'm Captain Skywalker. I'm a Scientist & my nature is Research, Explore and Develop.. I'm the founder & C.E.O of ASAI Inc. (Automation Systems with Artificial Intelligence)... My ultimate aim is to develop a Galactic Human Empire....\n "

    def Logic(self):
        return ">_  At the ultimate level, Everything Is Nothing because, this very universe itself doesn't have any purpose, It just is...\n"

    def Ultimate_Aim(self):
        return ">_  If Everything Is Nothing then, You have to do the greatest thing that you ever could & Which is developing a Galactic Human Empire for good, advancement and to improve the quality of life...\n"

    def Perfect(self):
        return ">_  There is nothing like perfect, It just the matter of the perseption of reality, Just be and build something better than ever that, You can proud of...\n"

    def Possibility(self):
        return "\n\t>_  Everything Is Possible through Technological Advancements...\n"


skywalker = Human()
print(skywalker.mindset)
print(skywalker.nature)
print(skywalker.work)
print(skywalker.thinking)

ultimate = Human()
print(ultimate.Intro())
print(ultimate.Logic())
print(ultimate.Perfect())
print(ultimate.Ultimate_Aim())
print(ultimate.Possibility())





