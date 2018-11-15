# Enter the radiue
# Use the Pythagorean theorem.
import sys
import math

def main():
    radius = int(sys.argv[1])

    for i in range(1, 2 * radius):
        s = ""
        dix = (i - radius) ** 2
        for j in range(1, 2 * radius):
            diy = (j - radius) ** 2
            dis = math.sqrt(dix + diy)
            if(dis <= radius):
                s += "o"
            else:
                s += " "
        print(s)
            


main()