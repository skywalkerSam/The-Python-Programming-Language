# Code Debugging...

'''
Best practices;

    >_  Use code editors/IDE.

    >_  Use linting like, pylint, pyflakes, etc..

    >_  Read errors & try to understand it, print out things you have doubt on...

    >_  Use Pdb (Python Debugger)  ;)

'''

import pdb

def add(num_one=0, num_two=0):
    pdb.set_trace()                             # pdb started, type <help> to get some help...
    answer = (int(num_one) + int(num_two))
    return answer


add()












