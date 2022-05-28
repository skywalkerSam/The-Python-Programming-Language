# You can also raise errors intentionally, of course...


from pyfiglet import *


def Intro():
    print(figlet_format("Error . . .", "script"))


while (True):
    try:
        Intro()
        raise Exception
        

    except Exception:
        print("\t You can't just fix me, I'm the greatest error of all space-times ;) ;) ;) \n")
        break



