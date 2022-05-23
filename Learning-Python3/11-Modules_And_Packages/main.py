# Main File

import module_one                   # a module
import packageOne.module_two        # a module from package

from packageOne.packageTwo.module_three import ultimate, star, Horizon     # Import a specfic functions from a module

from module_x import *      # Import all, no need to specify the module name along with the function name

import pyfiglet as pf        # Import pyfiglet using 'pf' as the module name



if __name__ == "__main__":          # So the code runs only on the main file, not the imported module's file
    module_one.Intro()
    packageOne.module_two.cool()

    ultimate()
    star()

    ex()


print(__name__)
print(type(packageOne.packageTwo.module_three.subject_one))     # It's the imported module's object, not __main__ !


print(module_one.processCommand.__doc__)        # Docstring




"""
# Modules & Packages in python ;)

    >_  Every python file is a module, to import it just call it's filename.

    >_  Multiple python files (modules) in a folder together, it's a package..

    >_  __init__.py file tells that It's a python package...

    >_  

"""

