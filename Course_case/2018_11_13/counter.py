import sys


def main(number):
    print_number(1, number)


def print_number(num1, num2):
    if num1 <= num2:
        print(num1)
        print_number(num1 + 1, num2)

main(int(sys.argv[1]))
