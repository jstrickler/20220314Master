from collections import namedtuple
from pprint import pprint

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person[0], person[1])

Person = namedtuple('Person', 'first_name last_name product dob')

person = Person('Bill', 'Gates', 'Microsoft', '1955-10-28')

print(person)
print(person.first_name, person.last_name)
print(person[0], len(person), type(person))



Knight = namedtuple('Knight', 'name title color quest comment')
knight_list = []
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight = Knight(name, title, color, quest, comment)
        knight_list.append(knight)
pprint(knight_list)
print()

for k in knight_list:
    print(k.title, k.name)
print()

print(Knight._fields)
print(dict(k._asdict()))
k = k._replace(title='poobah')
print(k)

