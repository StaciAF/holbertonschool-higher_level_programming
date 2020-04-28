#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "is"
greaterend = "and is greater than 5"
zero = "and is 0"
lessend = "and is less than 6 and not 0"

if number < 0:
    lastdig = number % -10
else:
    lastdig = number % 10

if lastdig > 5:
    print("{} {:d} is {:d} {}".format(str1, number, lastdig, greaterend))

elif lastdig == 0:
    print("{} {:d} is {:d} and is 0".format(str1, number, lastdig))

else:
    print("{} {:d} is {:d} {}".format(str1, number, lastdig, lessend))
