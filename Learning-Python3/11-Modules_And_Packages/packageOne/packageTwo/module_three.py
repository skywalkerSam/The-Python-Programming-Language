# Module - Three

from turtle import st
from pyfiglet import *


def ultimate():
    print(figlet_format("Space, The Final Frontier...", "script"))


def star():
    print(figlet_format("Star Wars", "big"))


ultimate()
star()



class Horizon():
    def __init__(self, name="Skywalker", type="Horizon", level=0) -> None:
        self._name = name
        self._type = type
        self._level = level

    
    def Intro(self):
        print(f"This is {self._name}. Type; {self._type}  Level; {self._level}")



subject_one = Horizon("Grogu", "Mandalorian\Jedi", 3)
subject_one.Intro()


print(__name__)
print(type(subject_one))     # Because it's created here so it is __main__
