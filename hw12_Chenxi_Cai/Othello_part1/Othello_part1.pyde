from tiles import Tiles
from board import Board
from gamemanager import GameManager

TOTAL_COLUMN = 4
TOTAL_ROW = 4
CELL_WIDTH = 100

tiles = Tiles(TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH)
board = Board(TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH)
gamemanager = GameManager(TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH)


def setup():
    size(TOTAL_COLUMN * CELL_WIDTH, TOTAL_ROW * CELL_WIDTH)


def draw():
    background(0, 127, 0)
    board.display()
    gamemanager.display()
    gamemanager.result()


def mousePressed():
    gamemanager.player_make_move(mouseX, mouseY)


def mouseReleased():
    noLoop()
    gamemanager.computer_make_move()
    delay(1000)
    loop()
