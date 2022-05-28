
# @classmethod  &  @staticmethod


class PlayerProfile:

    def __init__(self, name="user", age=0) -> None:
        self.name = name
        self.age = age


    @classmethod
    def add_values(cls, num1, num2):
        return (num1 + num2)   

    @staticmethod
    def add_nums(num1, num2):
        return(num1 + num2)



player1 = PlayerProfile("Capt_Skywalker", "16")
print(player1.name)
print(player1.age)
print(player1.add_values(33, 66))


#difference
player2 = PlayerProfile.add_values(3, 6)
print(player2)

player3 = PlayerProfile.add_nums(9, 6)
print(player3)


