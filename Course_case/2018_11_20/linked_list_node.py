class Node:
    """A linked list node"""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "["+self.value+"]->" + str(self.next)