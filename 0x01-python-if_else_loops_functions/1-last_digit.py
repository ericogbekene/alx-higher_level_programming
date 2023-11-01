#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
lastDigit = abs(number) % 10
#print("Last digit of {} is {}".format(number, lastDigit))

if lastDigit > 5:
    print("Last digit of {:d} is {} and is greater than 5".format(number, lastDigit))
elif lastDigit == 0:
    print("Last digit of {:d} is {} and is 0".format(number, lastDigit))
elif not 0 and lastDigit < 6:
    print(f"Last digit of {number:d} is {lastDigit} and is less than 6 and not 0")
