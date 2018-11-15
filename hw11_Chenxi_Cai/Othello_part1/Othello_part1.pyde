from tiles import Tiles

TOTAL_COLUMN = 4
TOTAL_ROW = 4
CELL_WIDTH = 100

tiles = Tiles(TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH)

def setup():
     size(TOTAL_COLUMN * CELL_WIDTH, TOTAL_ROW * CELL_WIDTH)

def draw():
    background(0, 127, 0)
    tiles.display()
    tiles.update()

def mousePressed():
    tiles.control(mouseX, mouseY)
