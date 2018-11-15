import sys


def main(number):
    print(add_up(number, 0, 0))


def add_up(number, counter, total):
    if(counter == number):
        return total
    else:
        counter += 1
        total = total + counter
        print(total)
        return add_up(number, counter, total)
        # Tail recursion should maintain some values so more than one arguments


main(int(sys.argv[1]))
