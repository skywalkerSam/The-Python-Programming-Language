
"""
Developer: Master Skywalker
Purpose: Dreamer Program
Stardate: 12021.295.09:01:00

"""


class Dreamer():
    def __init__(self, _name="Dreamer", _dream="A Million Dreams") -> None:
        self.name = _name
        self.dream = _dream

    def current_work(self):
        print(f"Working on Project-{self.dream}")

    def new_dream(self):
        pass


def DreamerOne():
    dreamer_one = Dreamer()
    print(dreamer_one.name)
    dreamer_one.current_work()


def DreamerTwo():
    dreamer_two = Dreamer("Skywalker", "Development Of Spacefaring Civilization")
    print(f"This is {dreamer_two.name}")
    dreamer_two.current_work()



DreamerTwo()


    











