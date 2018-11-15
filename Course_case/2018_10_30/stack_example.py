import sys
from stack_list import StackList
from stack_linkedlist import Stack


def main():
    stack = Stack()
    in_string = input("Input a string:\n")
    for ch in in_string:
        if ch == "a":
            stack.push(ch)
        elif ch == "b":
            if not stack.is_empty():
                stack.pop()
            else:
                print("REJECT")
                sys.exit()
    
    if stack.is_empty():
        print("ACCEPT")
    else:
        print("REJECT")


main()
