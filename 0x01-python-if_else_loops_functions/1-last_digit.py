#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number % 10 if number > 10 else number % -10
if i > 5:
    print(f"Last digit of {number:d} is {i} and is greater than 5")
elif i < 6 and i != 0:
    print(f"Last digit of {number:d} is {i} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {i} and is 0")
