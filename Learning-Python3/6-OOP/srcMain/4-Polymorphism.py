"""
# Polymorphism ;
            >_ Fourth & last pillar of OOP.
            >_ Poly (Many) - Morphism (Forms), Many Forms..

"""


class User():
    '''
    It's a class object named User...
    '''
    def __init__(self, name="Unknown", email="unknown@unknown.abc") -> None:
        """
        It's a constructor method...
        """
        self._name = name
        self._email = email


    def intro(self):
        """
        It gives the intoduction...
        """
        return (f"\tThis is {self._name}")
        

class Scientist(User):
    '''
    It's an Object-Scientist which has inherited the features of Object-User...
    '''
    def welcome(self):
        return (f"\n\t Hello {self._name}, Welcome to the mindset of Scientists where, we are developing Spacefaring Civilisation...\n")



user1 = Scientist("Murlidhar")
# print(user1.name)
print(user1.intro())
print(user1.welcome())


# Docstring...
print("Here's the docstring of Object-User;", User.__doc__)
print("Here's the docstring of Object-Scientist;",Scientist.__doc__)


user2 = Scientist("Shree")
# print(user2.intro())
print(user2.welcome())





"""
super(),
    >_ It gives the access to the functions of the parent classes, it's damm awesome!

"""

class Explorer(Scientist):
    def welcome(self):
        return super().welcome()


explorer_one = Explorer('Explorer Skywalker', 'explorerskywalker.asaiinc@gmail.com')
print('Name; ', explorer_one._name)
print("Email: ", explorer_one._email)
print(explorer_one.welcome())




"""
Introspection,
        >_ It show the functions which this instance has access to...
"""

# print(dir(explorer_one))





