class Spot:
    def _init_(self, x, y):
        self.x = x
        self.y = y
    
    def display(self):
        noStroke()
        fill(255)
        ellipse(self.x, self.y, 95, 95)
        fill(0)
        ellipse(self.x, self.y, 88, 88)
        fill(255)
        ellipse(self.x, self.y, 65, 65)
        fill(255, 0, 0)
        ellipse(self.x, self.y, 50, 50)
        fill(255)
        ellipse(self.x, self.y, 25, 25)
        fill(0)
        ellipse(self.x, self.y, 18, 18)
        
