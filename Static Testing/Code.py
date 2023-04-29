import random as r
import numpy as np
import matplotlib


def Function1(a):
    if a % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def Function2(b):
    if b % 3 == 0 and b % 5 == 0:
        print("FizzBuzz")
    elif b % 3 == 0:
        print("Fizz")
    elif b % 5 == 0:
        print("Buzz")


def Function3(a, b):
    return a + b


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print("The values are:", x, "and", y)

Function1(x)
Function2(y)
print(Function3(x, y))
