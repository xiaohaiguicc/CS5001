from node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = Node(item)
        node.next = self.top # 注意top node位置不变，每次把新的node加到开头，
        self.top = node # 然后top node指向新的头
    
    def pop(self):
        val = self.top.value
        self.top = self.top.next # 指向下一个，就相当于剔除了top项
        return val
    
    def peek(self):
        return self.top.value
    
    def is_empty(self):
        if self.top:
            return False
        else:
            return True