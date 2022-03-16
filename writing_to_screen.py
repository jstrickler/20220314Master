
person = "Tom Hanks"
city = "Jersey City"

value1 = 234.34939
value2 = 93.238023

print(person, city, value1, value2)    #  str(person) + ' ' + str(city) + ' ' + str(value) + '\n'
print("Done.")

print(person, city, value1, sep="/")
print(person, city, value1, sep="")
print(person, city, value1, sep=", ")

print(person, end=' ')
# if ...
print(city)
# else ...

print(person, "lives in", city)
print("{} lives in {}".format(person, city))
print(f"{person} lives in {city}")
print(person, "owes", value1)

print("{} owes {:.2f}".format(person, value1))
print(f"{person} owes {value1:.2f}")

big_number = 23905820395203958205859375297520572057295293
print(f"{big_number:,d}")
