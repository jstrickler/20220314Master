from datetime import date

jay_bd = date(2014, 8, 1)




person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person[0], person[1])

first_name, last_name, product, dob = person   # iterable unpacking

print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
#  list == table
#  tuple == row

print(type(people), type(people[0]), type(people[0][0]))
print("people[0]: {}".format(people[0]))
print("people[0][0]: {}".format(people[0][0]))
print("people[0][0][0]: {}".format(people[0][0][0]))

for person in people:
    # print(person)
    print(person[0], person[1])
print('-' * 60)

for first_name, last_name, product, dob in people:
    year, month, day = dob.split('-')
    birth_date = date(int(year), int(month), int(day))
    today = date.today()
    raw_elapsed_time = today - birth_date
    age = round(raw_elapsed_time.days / 365, 1)
    print(first_name, last_name, age)
print('-' * 60)

t3 = 'a', 'b', 'c'  # 3 elements
t2 = 'a', 'b'       # 2 elements
t1 = 'a',           # 1 element
t0 = ()             # 0 elements













for person in people:
    dob = person[-1]
    if (dob >= "1964") and (dob <= "1970"):
        print(person)




