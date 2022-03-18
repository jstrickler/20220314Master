from copy import deepcopy

colors = ['red', 'purple', 'pink']

x = colors

x.append('blue')
colors.append('yellow')
print("colors: {}".format(colors))
print("x: {}\n".format(x))

y = list(colors)  # new list from colors
y.append('black')
colors.append('green')
print("colors: {}".format(colors))
print("y: {}\n".format(y))

data = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [5, 10, 20],
]

d = data  #  alias
d.append([4.1, 5.2, 6.3])
print("data: {}".format(data))
print("d: {}".format(d))

d2 = list(data)  # shallow copy
d2.append(['cow', 'horse', 'pig'])
print("d2: {}".format(d2))
print("data: {}".format(data))

d2[0].append('wombat')
print("data: {}".format(data))
print("d2: {}\n".format(d2))

z = deepcopy(data)  # deep copy
data[1].append("honey badger")
print("z: {}".format(z))
print("data: {}\n".format(data))









