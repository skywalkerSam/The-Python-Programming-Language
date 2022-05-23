# Module - sys

import sys


# print(dir(sys))
# print(sys)

# sys.argv      - It works only if the file runs from the terminal with respective index

first_name = sys.argv[0]
last_name = sys.argv[1]

print(f"Hello, {first_name} {last_name}")





"""
# Like this;

PS A:\pythonProgramming> & C:/Users/samsk/anaconda3/python.exe a:/pythonProgramming/Python_Learning/11_MODULESandPACKAGES/02-sys_module.py ok done
Hello, ok done
PS A:\pythonProgramming> 

"""
