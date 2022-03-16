value = 70

if value > 75:
    print("koala")
    print("kangaroo")
elif value > 50:  # else if
    print("wombat")
    print("wallaby")
    if value > 63:
        print("blue-ringed octopus")
else:
    print("kookaburra")
    print("quokka")
    print("platypus")

print("Done.")

# x is Boolean false if
# x is False
# x in None
# x == 0   (or x == 0.0)
# len(x) == 0

debug = True

if debug:
    color = "red"
else:
    color = "green"


#  V1 if EXPR else V2
color = "red" if debug else "green"

#  == != > < >= <=


x = 23
name  = "Chad"

if (name == 'Chad') and (x > 15):
    print("waHOOwa")

if (name == 'Chad') or (name == 'Bernie'):
    print("OK")































