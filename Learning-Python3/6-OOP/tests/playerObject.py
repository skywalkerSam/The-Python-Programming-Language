# A Player Object...

class PlayerCharacter():
    def __init__(self, name="Unknown", group="Unknown", level=0) -> None:
        self._name = name
        self._group = group
        self._level = level


    def Intro(self):
        return (f"This is {self._name} from {self._group} group on level {self._level} :)")


    def SignIn(self):
        username = input("\t Enter your username: ")
        password = input("\t Enter your password: ")
        if (username=="True" and password=="True"):
            print("Signed In Successfully :) ")
        else:
            print("Ok, Just fill the required once...")



class Wizard(PlayerCharacter):
    def __init__(self, name="Unknown", group="Unknown", level=0) -> None:
        super().__init__(name, group, level)


    def attack(self):
        return ("Attacking with the wand...")


class Archer(PlayerCharacter):
    def __init__(self, name="Unknown", group="Unknown", level=0) -> None:
        super().__init__(name, group, level)

    
    def attack(self):
        total_arrows = 10
        arrows_left = total_arrows - 1
        total_arrows -= 1
        
        return (f"Attacking with the arrows, {arrows_left} arrows left...")

    
class Seeker(PlayerCharacter):
    def __init__(self, name="Unknown", group="Unknown", level=0) -> None:
        super().__init__(name, group, level)

    
    def attack(self):
        return ("Attacking with the flying broom...")


class Keeper(PlayerCharacter):
    def __init__(self, name="Unknown", group="Unknown", level=0) -> None:
        super().__init__(name, group, level)

    
    def attack(self):
        return ("Already defending the the goal...")

    
harry_potter = Wizard("Harry", "Wizard", 6)
print(harry_potter.Intro())

half_horse = Archer("Unicorn", "Archer", 3)
print(half_horse.Intro())
print(half_horse.attack())
half_horse.SignIn()




