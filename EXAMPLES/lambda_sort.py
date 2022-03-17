#!/usr/bin/env python

fruit = ["pomegranate", "cherry", "apricot", "date", "Apple",
         "lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
         "papaya", "FIG", "pear", "banana", "Tamarind", "persimmon",
         "elderberry", "peach", "BLUEberry", "lychee", "grape"]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

def ignore_case(e):
    return e.lower()

#  lambda param: return-value

fs1 = sorted(fruit, key=lambda e: e.lower())  # <1>
print("Ignoring case:")
print(' '.join(fs1))
print()

fs2 = sorted(fruit, key=lambda e: (len(e), e.lower()))  # <2>
print("By length, then name:")
print(' '.join(fs2))
print()

fs3 = sorted(nums)
print("Numbers sorted numerically:")
print("fs3: {}\n".format(fs3))

fs4 = sorted(nums, key=str)
print("fs4: {}\n".format(fs4))

