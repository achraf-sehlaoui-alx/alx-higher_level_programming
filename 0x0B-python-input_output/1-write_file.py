#!/usr/bin/python3
"""defining write_file with two args"""


def write_file(filename="", text=""):
    """reads filnams with utf-8"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
