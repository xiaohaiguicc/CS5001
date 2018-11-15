class Queue1:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items: # 如果这个不是空的
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if len(self.is_empty) == 0:
            return True
        else: 
            return False