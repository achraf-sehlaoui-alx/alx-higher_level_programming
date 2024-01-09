#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """ function that reads a text file UTF-8"""

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
