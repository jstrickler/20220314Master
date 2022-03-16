list1 = list()   # list(iterable)
print(list1)
s = "abc"
list2 = list(s)
print(list2)

list3 = ['red', 'purple', 'ecru', 'mauve']
print(list3)

list4 = list(list3)  # makes a copy of list3
print(list4)

list5 = list3   # does NOT make a copy of list3

cities = ['Jersey City', 'Durham', 'New York City', 'Loveland', 'Montreal']

print(cities[0], cities[3], len(cities))

cities.insert(0, 'Parsippany')
print("cities: {}".format(cities))
cities.insert(4, 'Birmingham')
print("cities: {}".format(cities))
cities.append('Houston')
cities.append("New Orleans")
print("cities: {}".format(cities))

more_cities = ['Akron', 'Pierre', 'Topeka']

cities.extend(more_cities)
print("cities: {}".format(cities))

#  LIST.insert(pos, value)  LIST.append(value)  LIST.extend(iterable)

del cities[0]
print("cities: {}".format(cities))

print(len(cities))

spam = ["spam", "spam", "spam", "spam", "spam", "spam", "spam", "spam", "eggs", "spam", ]
print(spam.count('spam'), spam.count('eggs'))
print(cities.count('Durham'))

cities.remove('Birmingham')
print("cities: {}".format(cities))

spam.remove('spam')
print("spam: {}".format(spam))

spam.remove('spam')
print("spam: {}".format(spam))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(5)
print("city: {}".format(city))
print("cities: {}".format(cities))

#  del LIST[pos]   LIST.pop()  LIST.pop(pos)  LIST.remove(value)

# spam.remove('ham')

print(cities[0], cities[7], cities[3])

print(cities[len(cities) - 1])
print(cities[-1], cities[-2])

print("cities: {}".format(cities))
print("cities[0:3]: {}".format(cities[0:3]))

#   start:stop   :stop   start:  start:stop:step
print("cities[:3]: {}".format(cities[:3]))
print("cities[5:]: {}".format(cities[5:]))

# start is INclusive
# stop is EXclusive

print("cities[3:5]: {}".format(cities[3:5]))

middle = len(cities) // 2
part1 = cities[:middle]
part2 = cities[middle:]
print(part1, part2)

cities.append('Sacramento')
middle = len(cities) // 2
part1 = cities[:middle]
part2 = cities[middle:]
print(part1, part2)

city = 'New York City'
print(city[:3])
print(city[4:8])
print(city[-4:])

print(city[::2])
print(city[::3])
print(city[::4])
print('-' * 60)

# for var, ... in iterable:
#    code
#    code
#    ...
for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city)
print()


s = "abc"
for char in s:
    print(char)
print()

for city in cities:
    print(city)
    if city == "Montreal":
        break

















