from spot import Spot
from stack import Stack

to_draw = Stack()
def setup():
    size(500, 250)

def draw():
    background(100)
    for spot in to_draw.content:
        spot.dispaly()

    # s = Spot(250, 200)
    # s.display()
    # noStroke()
    # fill(255, 120, 220)
    # ellipse(mouseX, mouseY, 100, 100)
    
def mousePressed():
    to_draw.push(Spot(mouseX, mouseY))

def keyPressed():
    if key == "x" or key == "X":
        to_draw.pop()
        print("Undo the last added spot")
