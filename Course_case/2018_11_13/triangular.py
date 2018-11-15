import sys


def main(number):
    print(add_up(number))


def add_up(number):
    if (number == 0):
        return 0
    return number + add_up(number - 1)  # head recursion


main(int(sys.argv[1]))
