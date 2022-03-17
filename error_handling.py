
file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        for line in file_in:
            print(line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    print(err)
    # set good value
    # log err
    # etc
except TypeError as err:
    print(err)
print('-' * 60)

with open('DATA/breakfast.txt') as breakfast_in:
    all_food = [line.rstrip() for line in breakfast_in]

try:
    print(all_food[33])
except IndexError as err:
    print(err)
print('-' * 60)

nums = [800, 0, 80, 1000, 32, "123", 255, 400, 5, 5000]

for num in nums:
    try:
        result = 10000 / num
    except (TypeError,ZeroDivisionError) as err:
        print(err)
    else:
        print(result)

print('-' * 60)


try:
    pass  # connect to something ...
except Exception as err:  # trap some exception
    pass
finally:  # do this whether or not an exception is raised
    pass


print("ALL DONE!")
