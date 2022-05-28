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
    def __init__(self, name="Unknown", group="Unknown", fitness_payoffs=0) -> None:
        self._name = name
        self._group = group
        self._payoffs = fitness_payoffs


    def Introduction(self):
        return (f"This is {self._name} from {self._group} group with {self._payoffs} fitness payoffs :)")


    def power(self):
        return (f"{self._name} are powerful with the wand...")


class Archer(PlayerCharacter):
    def __init__(self, name="Unknown", group="Unknown", level=0, total_arrows=10) -> None:
        self._name = name
        self._group = group
        self._level = level
        self._arrows = total_arrows
        

    def attack(self):
        self._arrows -= 1
        return (f"Attacking with the arrows, {self._arrows} arrows left...")

    
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

    
# Wizard
harry_potter = Wizard("Harry", "Wizard", 5)
print(harry_potter.Introduction())
print(harry_potter.power())


# Archer
half_horse = Archer("Unicorn", "Archer", 3, 7)
print(half_horse.Intro())
print(half_horse.attack())
# half_horse.SignIn()




# Multiple Inheritance...
class Cyborg(Wizard, Archer):
    def __init__(self, name="Unknown", group="Unknown", level=0) -> None:
        self._name = name
        self._group = group
        self._level = level

        # To use specfic attribute of any class, specify it...
        Archer.__init__(self, total_arrows=10)

        
optimus = Cyborg("Optimus v1.0", "'Argumented Cyborg'", 1)
print(optimus.Intro())
print(optimus.power())
print(optimus.attack())
optimus.SignIn()
 