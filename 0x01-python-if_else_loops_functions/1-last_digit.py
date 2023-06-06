#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_s = str(number)
last_ = abs(number) % 10

if int(number) < 0:
    last_ = -last_

if last_ > 5:
    print(f"Last digit of {number_s} is {last_} and is greater than 5")
elif last_ == 0:
    print(f"Last digit of {number_s} is {last_} and is 0")
else:
    print(f"Last digit of {number_s} is {last_} and is less than 6 and not 0")
