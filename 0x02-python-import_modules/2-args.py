#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    z = len(sys.argv)
    if z == 1:
        print("{} arguments.".format(z - 1))
    elif z == 2:
        print("{} argument:".format(z - 1))
    else:
        print("{} arguments:".format(z - 1))
    for i in range(1, z):
        print("{}: {}".format(i, sys.argv[i]))
