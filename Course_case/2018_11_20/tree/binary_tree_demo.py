from binary_tree import BinaryTree


def main():
    my_binary_tree = BinaryTree('A')
    print(my_binary_tree)

    my_binary_tree.add_val_l('B')
    print(my_binary_tree)

    my_binary_tree.add_val_l('C')
    print(my_binary_tree)

    my_binary_tree.add_val_l('D')
    print(my_binary_tree)

    my_binary_tree.add_val_r('E')
    print(my_binary_tree)

    my_binary_tree.add_val_r('F')
    print(my_binary_tree)

    if my_binary_tree.contains('E'):
        print("This tree contains 'E'")
    else:
        print("This tree does not contain 'E'")

    if my_binary_tree.contains('J'):
        print("This tree contains 'J'")
    else:
        print("This tree does not contain 'J'")

main()