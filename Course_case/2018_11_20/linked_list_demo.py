from linked_list import LinkedList


def main():
    my_linked_list = LinkedList(['A'])
    my_linked_list.extend('B')
    my_linked_list.extend('C')
    my_linked_list.extend('D')
    my_linked_list.insert('Z')
    print(my_linked_list)

    my_linked_list2 = LinkedList("A string will work")
    print(my_linked_list2)

    # How about removing last? We have direct access to the last node,
    # but not to its previous node
    last = my_linked_list2.remove_last()
    print(last)
    print(my_linked_list2)

    last = my_linked_list2.remove_last()
    print(last)
    print(my_linked_list2)

    last_node = my_linked_list2.remove_last()
    print(last_node)
    print(my_linked_list2)

    if my_linked_list2.contains('s'):
        print("This linked list contains 's'")
    else:
        print("This linked list does not contain 's'")

    if my_linked_list2.contains('z'):
        print("This linked list contains 'z'")
    else:
        print("This linked list does not contain 'z'")


main()