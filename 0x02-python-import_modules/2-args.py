#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    z = len(sys.argv)
    if z == 1:
        print("0 arguments.")
    elif z == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(z - 1))
    for i in range(1, z):
        print("{}: {}".format(i, sys.argv[i]))
