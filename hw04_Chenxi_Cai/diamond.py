import sys
import math


def main():
    height = int(sys.argv[1])
    space_num = math.ceil(height / 2) # The number of space before *
 
    # Top half
    for h in range(1, math.ceil(height / 2) + 1, 1):
        space_num -= 1
        print(" " * space_num + "*" * (2 * h - 1))

    # If odd-numbered lines, space number starts at 1
    # If even-numbered lines, space number starts at 0  
    space_num += height % 2 

    # Bottom half
    for h in range(math.floor(height / 2), 0, -1):
        print(" " * space_num + "*" * (2 * h - 1))
        space_num += 1
        

main()