# Directory management in FileIO...

"""
# Directory management:
                    >_ ./abc/xyz    - Start from current folder.

                    >_ ../123/abc   - Start from a directory back..

                    >_ Use "pathlib" library, It's cross-platform & doesn't depends on the OS of the system...

"""

'''
# ./
with open("files/hello.sh", "w") as sh_file:
    sh_file.write("echo 'Hello World...'")

with open("./files/matrix/matrix.cpp", "w") as cpp_file:
    cpp_file.write("#include <iostream>")

with open("./files/matrix/matrix.cpp", "a") as cpp_file:
    cpp_file.write("\n\nstd::cout<<3*3;\n")

with open("./files/matrix/matrix.cpp") as cpp_file:
    print(cpp_file.read())
'''


# ../
with open("../hello.sh", "w") as my_file:
    my_file.write("\n echo 'I am Starboy'")

with open("../hello.sh") as shell_file:
    print(shell_file.read())
