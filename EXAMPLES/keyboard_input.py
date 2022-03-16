#!/usr/bin/env python

user_name = input("What is your name: ")
quest = input("What is your quest? ")
print("{} seeks {}".format(user_name, quest))

raw_num = input("Enter number: ")  # <1>
try:
    num = float(raw_num)  # <2>
except ValueError as err:
    print(err)
else:
    print("2 times {} is {}".format(num, 2 * num))
