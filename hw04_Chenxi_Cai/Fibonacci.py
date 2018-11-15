import sys

def main():
    num = int(sys.argv[1])
    fib_list = [0, 1]

    for i in range(2, num, 1):
        fib_new = fib_list[i - 2] + fib_list[i - 1]
        fib_list.append(fib_new)

    print("The first N Fibonacci sequence where N is %d:\n" % num, fib_list)


main()