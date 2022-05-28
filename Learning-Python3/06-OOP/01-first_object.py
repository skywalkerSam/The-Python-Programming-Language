    
"""

Creating the first object/instance ;

"""

# blueprint
class PlayerCharacter:
    def __init__(self, name, age=16):  
        self.name = name    # attributes /properties /parameters
        self.age = age

    def start(self):
        return "\nStarting Instance Using The Blueprint..."

# individual instances
player1 = PlayerCharacter("Captain", "17")
print(player1)
print(player1.name)
print(player1.age)

player2 = PlayerCharacter("Skywalker", "18")
print(player2)
print(player2.name)
print(player2.age)

player3 = PlayerCharacter("Tron")
print(player3.start())
# print(player3)
print(player3.name)
print(player3.age)

player3.value = 2010
print("First Appeared...", player3.value)



