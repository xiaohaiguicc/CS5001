class Node:
    """A binary tree node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return (self.value +
                " (" + str(self.left) + ", " + str(self.right) + ")")