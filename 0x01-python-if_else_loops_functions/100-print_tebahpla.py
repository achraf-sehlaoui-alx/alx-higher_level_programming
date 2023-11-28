#!/usr/bin/python3
for i in range(ord('z'), ord('a'), -1):
    if i % 2:
        i = i - 32
    print("{:c}".format(i), end="")
