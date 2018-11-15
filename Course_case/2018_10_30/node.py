class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def _repr_(self):
        return "[" + self.value+"]->" + self.next.__repr__() # a recursion, when next is None, it stops