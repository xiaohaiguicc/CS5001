from node import Node

class Queue2:
    def __init__(self):
        self.first = None
        self.last = None
    
    def __repr__(self):
        return self.first.__repr__()
    
    def enqueue(self, value):
        node = Node(value)
        if self.first:
            self.last.next = node # 接在最后，然后让last node后移为新加的那个node
            self.last = self.last.next
        else:
            self.first = node # 第一次enqueue
            self.last = self.first # 这句别忘了，当只有一个node时，first node就是last node

    def dequeue(self):
        val = self.first.value
        self.first = self.first.next
        return val

    def peek(self):
        return self.first.value

    def is_empty(self):
        if self.first:
            return True
        else: 
            return False