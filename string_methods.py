
actor = "Chris Hemsworth"

print(actor, type(actor), len(actor))

print(actor.upper())

a1 = actor.upper()
a2 = actor.lower()
print(a1, a2)
actor.upper()
print("actor: {}".format(actor))
print("actor.count('h'): {}".format(actor.count('h')))
print("actor.count('hem'): {}".format(actor.count('hem')))
print("actor.lower().count('h'): {}".format(actor.lower().count('h')))

print("actor.startswith('Chris'): {}".format(actor.startswith('Chris')))
print("actor.startswith('Liam'): {}".format(actor.startswith('Liam')))
print("actor.lower().startswith('chris'): {}".format(actor.lower().startswith('chris')))

print("'hem' in actor: {}".format('hem' in actor))
print("'wombat' in actor: {}".format('wombat' in actor))

print("actor.find('Hem'): {}".format(actor.find('Hem')))
print("actor.find('wombat'): {}".format(actor.find('wombat')))

s = "      \n     Python beats Rust\t\t    "
print("|" + s.lstrip() + "|")  # strips \n \r \t \f \b
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s2 = "xyxxxyyyxxyyxxxxxxxxxyyyyyyPython beats Rustyyyyyyyyxxxxxxxxxyxyxyxyxyyyyyxxxx"
print("|" + s2.lstrip("xy") + "|")  # strips \n \r \t \f \b
print("|" + s2.rstrip("xy") + "|")
print("|" + s2.strip("xy") + "|")
print()

print(s.strip().replace(' ', '-'))

print(actor.replace('h', 'TOMATO'))
print(actor.replace('h', 'TOMATO', 1))










