import time as t
from os import path
from sys import argv
from sys import exit

first, second, third = argv

if len(argv) < 2:
    print "error accuired\n You must specify only 1 file name and optional argument"

def create_file(filename):
    if not path.isfile(filename) or path.isfile(filename) and third == '-r':
        with open(filename, 'w') as f:
            f.write("\n" * 30 + "kappa\t" * 3)
    else:
        print "file has already exist"
        exit(0)


if __name__ == '__main__':
    create_file(second)
    print "Done"
