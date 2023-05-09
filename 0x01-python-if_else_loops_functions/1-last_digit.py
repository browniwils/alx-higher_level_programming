#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lucky = abs(number) % 10
if number < 0:
    lucky *= -1
print(f"Last digit of {number:d} is {lucky:d} and is ", end="")
if lucky > 5:
    print("greater than 5")
elif lucky == 0:
    print(0)
else:
    print("less than 6 and not 0")
