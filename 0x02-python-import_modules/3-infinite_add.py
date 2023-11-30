#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    s = 0
    z = len(sys.argv)
    for i in range(1, z):
        s += int(sys.argv[i])
    print(s)
