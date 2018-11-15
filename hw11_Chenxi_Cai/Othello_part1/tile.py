class Tile:
    """A tile"""
    def __init__(self, column, row, color, CELL_WIDTH):
        self.column = column
        self.row = row
        self.color = color
        self.CW = CELL_WIDTH

    def display(self):
        """Draws the tile"""
        fill(self.color)
        ellipse(self.column * self.CW + self.CW / 2,
                self.row * self.CW + self.CW / 2, 90, 90)
