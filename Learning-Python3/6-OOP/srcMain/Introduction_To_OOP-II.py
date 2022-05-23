
# object blueprint

class User:
    def __init__(self, username="guest", password="guest"):
        self.username = username    # attributes / properties
        self.password = password


user1 = User()
print(user1.username)
print(user1.password)

print("\n")

user2 = User("Captain", "helloworld")
print(user2.username)
password = user2.password
password_length = len(password)
print("X" * password_length)


'''
# Help

help(user2)
                -> Get help with a blueprint of users2.

                -> self.XYZ  is most important for the dynamic nature of any OOP code...

'''




'''
Attributes & Methods ;

'''

class universe:
    # Object class attribute
    human = True    
    # Constructor
    def __init__(self, name="user", age=0) -> None:
        # Dynamic attributes
        self.name = name
        self.age = age

    # Method
    def concious(self, human=True, robot=False):
        # Condition based queries
        if (human):
            return "Welcome to the future...\n"
        elif (robot):
            return "Robot, prove that you are concious..."
        else:
            return "Access Denied!"


# Instanciating objects
# Object-1
user1 = universe("Captain", 16)
print(user1.human)
print(user1.name)

print(user1.concious(False, True))
print(user1.concious())

# Object-2
user2 = universe()
print(user2.human)
print(user2.concious())






"""
 __init__

    -> Instanciate

"""

class driver:
    # __init__
    def __init__(self, name="user", age=0) -> None:
            self.name = name
            self.age = age
        

user1 = driver("Jassie Quick", 19)
print(user1.name)
print(user1.age)



