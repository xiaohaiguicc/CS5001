from linked_list_node import Node


class LinkedList:
    def __init__(self, python_seq):
        if len(python_seq) == 0:
            self.first = None
            self.last = None
        else:
            node = Node(python_seq[0])
            self.first = node
            self.last = node
            for n in python_seq[1:]:
                self.extend(n)

    def __repr__(self):
        return("linked_list("+str(self.first)+")")

    def extend(self, value):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def insert(self, value):
        node = Node(value)
        node.next = self.first
        self.first = node

    def remove_last(self):
        return self.remove_last_node(self.first).value

    def remove_last_node(self, node):
        if node.next is None:
            last = node
            node = None
            return last
        elif node.next.next is None:
            last = node.next
            node.next = None
            return last
        else:
            return self.remove_last_node(node.next)

    def contains(self, value):
        return self.contains_node(self.first, value)

    # Recursively defined contains_node
    def contains_node(self, node, value):
        if node.value == value:
            return True
        elif node.next:
            return(self.contains_node(node.next, value))
        else:
            return False