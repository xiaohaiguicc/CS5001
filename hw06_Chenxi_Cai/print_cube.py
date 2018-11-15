"""
Drawing the cube
A horizontal edge is drawn with - and requires 2n characters.
A vertical edge is drawn with | and requires num characters.
A vertical edge is drawn with / and requires num/2 characters.
Corners are drawn with +.
"""

def  hori_edge(space, num):
    """
    Draw horizontal edge

    Keyword Arguments:
    space -- the space before "+"
    num -- 2n is the number of "-"
    """
    print(" " * space + "+" + "-" * 2 * num + "+", end="")

def top(num):
    """
    Draw top part of cube
    1 - 2 "+" line part
    """
    space = num // 2 + 1
    hori_edge(space, num)
    print("\n", end="")
    for i in range(num // 2):
        print(" " * (space - 1 - i) + "/"
              + " " * 2 * num + "/" + " " * i + "|")

    hori_edge(0, num)
    print(" " * (num // 2) + "|")

def middle(num):
    """
    Draw middle part of cube
    2 - 3 "+" line part
    """
    ver_left = num - 1 - num // 2 # remaining "|"

    for i in range(ver_left):
        print("|" + " " * 2 * num + "|"
              + " " * (num // 2) + "|")

    print("|" + " " * 2 * num + "|" + " " * (num // 2) + "+")

def bottom(num):
    """
    Draw bottom part of cube
    3 - 4 "+" line part
    """
    for i in range(num // 2):
        print("|" + " " * 2 * num + "|"
              + " " * (num // 2 - i - 1) + "/")
    hori_edge(0, num)

def main():
    num = int(input("Input cube size (multiple of 2): "))
    top(num)
    middle(num)
    bottom(num)

main()
