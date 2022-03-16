i = 0
while i < 3:
    print(i)
    i += 1

print('-' * 60)


while True:
    name = input("Enter your name (or q to quit): ")
    if name == 'q':
        break  # exit loop
    if name == '':
        continue  # go to top
    print(f"Hello, {name}")

