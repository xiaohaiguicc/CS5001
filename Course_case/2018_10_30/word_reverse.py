import sys
from stack_linkedlist import Stack


def main():
    stack = Stack()
    in_string = input("Input a string:\n")
    out_string = ""
    for c in in_string:
        stack.push(c)
    while not stack.is_empty():
        out_string += stack.pop()

    print(out_string)


main()