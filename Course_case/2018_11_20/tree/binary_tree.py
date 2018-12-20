from binary_tree_node import Node


class BinaryTree:
    def __init__(self, val):
        self.root = Node(val)

    def __repr__(self):
        return str(self.root)

    def add_val_l(self, val):
        n = Node(val)
        self.add_node_l(self.root, n)

    def add_node_l(self, current_node, new_node):
        if (current_node.left is None):
            current_node.left = new_node
        elif (current_node.right is None):
            current_node.right = new_node
        else:
            self.add_node_l(current_node.left, new_node)

    def add_val_r(self, val):
        n = Node(val)
        self.add_node_r(self.root, n)

    def add_node_r(self, current_node, new_node):
        if (current_node.right is None):
            current_node.right = new_node
        elif (current_node.left is None):
            current_node.left = new_node
        else:
            self.add_node_r(current_node.right, new_node)

    def contains(self, value):
        return self.contains_node(self.root, value)

    def contains_node(self, node, value):
        if (node is not None) and (node.value == value):
            return True
        else:
            if node.left is not None:
                if self.contains_node(node.left, value):
                    return True
            if node.right is not None:
                if self.contains_node(node.right, value):
                    return True
        return False