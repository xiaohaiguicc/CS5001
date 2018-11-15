class Stack:
    def _init_(self):
        self.content = []
    
    def push(self, item):
        self.content.append(item)
        
    def pop(self):
        if len(self.content) > 0:
            return self.content.pop()
