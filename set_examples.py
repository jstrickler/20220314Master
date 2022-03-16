mary_countries = ['Spain', 'Burkina Faso', 'Japan', 'UK', 'UK', 'UK', 'Morocco',
                  'Portugal', 'Italy', 'Romania', 'Laos', 'Indonesia', 'Morocco',
                  'Brazil', 'Mozambique']

fred_countries = ['Japan', 'Japan', 'Kenya', 'Turkmenistan', 'Burkina Faso',
                  'Greece', 'Montenegro', 'Bulgaria', 'Romania', 'Portugal',
                  'Morocco']

mary = set(mary_countries)
fred = set(fred_countries)
fred.add('Spain')

print("mary: {}\n".format(mary))
print("fred: {}\n".format(fred))

print("Both:", mary & fred)  # intersection
print("Only one:", mary ^ fred)  # Xor
print("ALL:", mary | fred)  # union
print("Fred only:", fred - mary)
print("Mary only:", mary - fred)

if 'Canada' in mary:
    print("Mary has been to the great white north")

