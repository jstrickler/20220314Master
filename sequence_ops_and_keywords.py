

a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
c = a + b
print("c: {}".format(c))

f = "foo" + "bar"
print("f: {}".format(f))

dashes = '-' * 60  # or 60 * '-'
print("dashes: {}".format(dashes))

print("wombats" * 20)

flag_array = [True] * 25
print("flag_array: {}".format(flag_array))

junk = ['spam', 'ham']
print(junk * 3)
print()

colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

for color in 'orange', 'mauve', 'ecru', 'black', 'pink':
    print(color, color in colors)
print()

s = "spaghetti"
print('pag' in s)
print('page' in s)
print('page' not in s)

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(colors), min(colors), max(colors), sorted(colors), '\n')
print(len(nums), min(nums), max(nums), sorted(nums), sum(nums), '\n')

colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

rev_colors_gen = reversed(colors)
print(rev_colors_gen)
for color in rev_colors_gen:
    print(color)
print("Done.")
for color in rev_colors_gen:
    print(color)
print("Done again.")

rev_colors_gen = reversed(colors)
rev_colors = list(rev_colors_gen)
print(rev_colors)

rev_colors = list(rev_colors_gen)
print(rev_colors)
print()

for i, color in enumerate(colors):
    print(i, color)
    if i == 4:
        print("   BOOM!")

print(list(enumerate(colors)), '\n')

capitals = ['Helena', 'Sacramento', 'Annapolis', 42]
states = ['MT', 'CA', 'MD', 100.9]
nums = [5, 82, 98.6, 'wombat', 'pachyderm', 'bugsniffle']

state_caps = zip(states, capitals, nums)
print(list(state_caps), '\n')

for state, capital, num in zip(states, capitals, nums):
    print(state, capital, num)
print()

words = ['tra', 'la', 'la']

for i, word in enumerate(words, 1):
    print(i, word)
print()

#  range(stop)  range(start, stop) range(start, stop, step)

for i in range(10):
    print(i, 'wombat')
print()

for i in range(1, 11):
    print(i, 'Python') # , end='\n')
print()

for i in range(5, 101, 5):
    print(i, end=' ')  # default: end='\n'
print('\n')









