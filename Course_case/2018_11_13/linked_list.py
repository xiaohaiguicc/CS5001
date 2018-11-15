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
            for n in python_seq[1:]
                self.extend(n)
    

    def __repr__(self):
        return("Linked_List["+str(self.first)+"]")
    
    def extend(self, value):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            first.next