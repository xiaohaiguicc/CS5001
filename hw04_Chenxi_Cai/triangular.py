import sys

def main():
    num = int(sys.argv[1])

    tria_num = num * (num + 1) / 2

    print("The triangular number of input number %d is:" % num, tria_num)

main()