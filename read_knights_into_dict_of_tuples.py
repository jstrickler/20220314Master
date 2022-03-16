from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

print(knight_data['Galahad'][0])
print(knight_data['Lancelot'][2])
print()


#  for key, value in DICT.items(): ...
for name, values in knight_data.items():
    print(values[0], name)
print()




