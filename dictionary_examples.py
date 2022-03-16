
d1 = dict()   # empty dict
d2 = {'AK': 'Juneau', 'NC': 'Raleigh', 'VA': 'Richmond'}
d3 = {}

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['YCC'])
print(airports.keys())
print(airports.values())

airports['YUL'] = 'Montreal'

print(airports['YUL'])


print(airports.get('LAX'))
print(airports.get('LAX', 'NOT FOUND'))
print()

for abbr in 'LAX', 'RDU', 'MONKEY', 'SJO', 'FREAK', 'YYZ':
    print(abbr, abbr in airports)
print()

info = [('ORD', 'Chicago'), ('CMH', 'Columbus, OH'), ('BOS', 'Boston'),
        ('EWR', 'Newark, NJ'), ('OAK', 'Land of Oaks'), ('RDU', 'Durham')]

for abbr, name in info:
    print(abbr, airports.setdefault(abbr, name))
print()

print(airports, '\n')

airports['SEA'] = 'Seattle-Tacoma'
airports['PDX'] = 'Portland'

print(airports, '\n')

del airports['EWR']

print("airports: {}\n".format(airports))

for abbr, city in airports.items():
    print(abbr, city)
print('-' * 60)

for abbr, city in sorted(airports.items()):
    print(abbr, city)
print('-' * 60)


