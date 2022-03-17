"""
Routines for geometric calculations

circle_area() -- takes diameter as a float, returns area
rectangle_area() -- takes length and width, returns area

Blah blah
blah blah
"""
from math import pi

def circle_area(diameter):
    """
    Calculate area of circle, given the diameter.

    :param diameter: Diameter of circle as float
    :return: Area of circle as float
    """
    if isinstance(diameter, (float, int)):
        radius = diameter / 2
        return pi * (radius ** 2)
    else:
        raise TypeError("Diameter must be numeric")

def rectangle_area(length, width):
    """
    Calculate area of rectangle, given the length and width.

    :param length: Length of one side
    :param width: Length of other side
    :return: Area of rectangle as float
    """
    return length * width

if __name__ == '__main__':
    # only if run as script, NOT imported as module
    print("HI MOM!!")
    a = rectangle_area(10, 20)
    print("a: {}".format(a))

