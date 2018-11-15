class StackList:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        val = self.items[-1]
        self.items = self.items[:-1]
        return val
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
