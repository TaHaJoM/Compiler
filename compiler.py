#!/usr/bin/python3
import os
import sys

py_version = "3.8"

if sys.argv[1] == "install":
    os.system("sudo apt update")
    os.system("sudo apt install build-essential")
    os.system("python3 -m pip install cython")
else:
    os.system("cython --embed {}".format(sys.argv[2]))
    if sys.argv[1] == "c":
        cfile = sys.argv[2].split(".py")
        os.system(f"gcc $CFLAGS -I/usr/include/python{py_version}    -o {cfile[0]} {cfile[0]}.c -lpython{py_version} -lpthread -lm -lutil -ldl")
        os.system(f"rm {cfile[0]}.c")
        print("Done succesfully!!")
    elif sys.argv[1] == "s":
        cfile = sys.argv[2].split(".py")
        os.system(f"gcc -c -I/usr/include/python{py_version} -Wall -Werror -fpic {cfile[0]}.c")
        os.system(f"gcc -shared -I/usr/include/python{py_version} -o {cfile[0]}.so {cfile[0]}.o")
        os.system(f"rm {cfile[0]}.o {cfile[0]}.c")
        print("Done succesfully!!")
    else:
        print("Wrong Command!!!")
