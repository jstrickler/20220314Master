from collections import defaultdict
from pprint import pprint

def zero():
    return 0


info = defaultdict(zero)    #   defaultdict(lambda: 0)
info['spam'] = 12
info['ham'] = 85
info['eggs'] = 44

print(info['spam'], info['ham'])
# print(info.get('toast', 0))

print(info['toast'])
print(info['collywobbles'])
print(info['wombat'])

print("info: {}".format(info))

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fruit_info = defaultdict(list)
for fruit in fruits:
    first_letter = fruit[0]
    fruit_info[first_letter].append(fruit)

pprint(fruit_info)






