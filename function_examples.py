from math import pi

def get_message():  # business logic -- no user interaction
    return "Hello, Python world"

message = get_message()

print(message)

def display_message():  # display logic AKA presentation logic AKA UX (user experience) AKA UI
    message = get_message()
    print(message)

display_message()

def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

print(circle_area(5))
a = circle_area(123.456)
print("a: {}".format(a))

a2 = rectangle_area(10, 12.5)
print("a2: {}".format(a2))

# print(rectangle_area(42))

def greet(whom="world"):
    print("Hello,", whom)

greet('Mom')
greet("Uncle Ernie")
greet()


#         pos          named
#         req     opt  req     opt
def wacky(p1, p2, *p3, p4, p5, **p6):
    print("p1: {}".format(p1))
    print("p2: {}".format(p2))
    print("p3: {}".format(p3))
    print("p4: {}".format(p4))
    print("p5: {}".format(p5))
    print("p6: {}".format(p6))
    print('-' * 60)

wacky(5, 10, p4=15, p5=20)
wacky(5, 10, 20, 21, 22, 23, p4=15, p5=20, animal="wombat", country="Australia", city="Canberra")





