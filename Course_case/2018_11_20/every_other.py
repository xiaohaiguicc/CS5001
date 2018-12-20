
import sys
from linked_list import LinkedList


def every_other(linked_list):
    e_o = LinkedList('')
    return every_other_node(e_o, linked_list.first)


def every_other_node(e_o, node):
    e_o.extend(node.value)
    if node.next: 
        if node.next.next:
            every_other_node(e_o, node.next.next)
    return e_o


def main():
    linked_list = LinkedList(sys.argv[1])
    print(every_other(linked_list))


main()