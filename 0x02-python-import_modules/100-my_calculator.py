#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    z = len(sys.argv)
    if z != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        p = sys.argv[2]
        if p == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif p == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif p == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif p == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
