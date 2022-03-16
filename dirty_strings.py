#!/usr/bin/python3

spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup(s):
    pass

for dirty_string in spam:
    clean_string = cleanup(dirty_string)
    print(f"BEFORE: |{dirty_string}| AFTER: |{clean_string}|")
