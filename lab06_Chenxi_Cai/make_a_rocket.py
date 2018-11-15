"""
arguments:
numbers representing the width of the rocket in characters
the length of the rocket's fuselage in square segments
either left blank (not given) or will be the word "striped"
"""
import sys


def cone(width):
    """
    define the nose cone configuration

    keyword argument:
    width -- rocket's width
    """
    height = (width - 1) // 2
    space = (width - 1) // 2
    for i in range(height):
        print(" " * space + "*" * (2 * i + 2 - width % 2))
        space -= 1


def tail(width):
    """
    define the tail configuration

    keyword argument:
    width -- rocket's width
    """
    line1 = width // 2
    space = (width - line1) // 2
    while line1 != width:
        print(" " * space + "*" * line1)
        space -= 1
        line1 += 2
    print("*" * width + "\n" + "*" * width)


def fuselage(width, length, striped=None):
    """
    define the segment structure for the fuselage

    keyword argument:
    width -- rocket's width
    length -- the length of the rocket's fuselage
    striped -- whether half with _ characters
    """
    if striped is None:
        for i in range(width * length):
            print("X" * width)
    else:
        upper_line = width // 2
        lower_line = width - upper_line
        for i in range(length):
            for j in range(upper_line):
                print("_" * width)
            for j in range(lower_line):
                print("X" * width)


def main():
    width, length = int(sys.argv[1]), int(sys.argv[2])
    cone(width)
    if len(sys.argv) == 3:
        fuselage(width, length)
    else:
        fuselage(width, length, True)

    tail(width)


main()
