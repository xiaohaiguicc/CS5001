class Board:
    """Draws the board"""
    def __init__(self, TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH):
        self.TC = TOTAL_COLUMN
        self.TR = TOTAL_ROW
        self.CW = CELL_WIDTH

    def display(self):
        """Display board"""
        for i in range(1, self.TC):
            strokeWeight(2)
            line(i * self.CW, 0, i * self.CW, self.TR * self.CW)
        for i in range(1, self.TR):
            strokeWeight(2)
            line(0, i * self.CW, self.TC * self.CW, i * self.CW)
