import os.path as p
import os
from time import sleep
from os import _exit as exit
def Main():
    if(p.exists("CMakeLists.txt")):
        os.system("cmake CMakeLists.txt")
    else:
        exit(4454)

if __name__ == "__main__":
    Main()