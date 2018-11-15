from tile import Tile


class Tiles:
    """A collection of tiles"""
    def __init__(self, TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH):
        self.TC = TOTAL_COLUMN
        self.TR = TOTAL_ROW
        self.CW = CELL_WIDTH
        self.WHITE = 225
        self.BLACK = 0
        self.COLOR = [225, 0]
        self.white_count = 2
        self.black_count = 2
        self.tiles_list = [[0] * self.TR for i in range(self.TC)]
        self.tiles_list[1][1] = Tile(1, 1, self.WHITE, self.CW)
        self.tiles_list[2][2] = Tile(2, 2, self.WHITE, self.CW)
        self.tiles_list[2][1] = Tile(2, 1, self.BLACK, self.CW)
        self.tiles_list[1][2] = Tile(1, 2, self.BLACK, self.CW)

    def display(self):
        """Display the board"""
        for i in range(1, self.TC):
            strokeWeight(2)
            line(i * self.CW, 0, i * self.CW, self.TR * self.CW)
        for i in range(1, self.TR):
            strokeWeight(2)
            line(0, i * self.CW, self.TC * self.CW, i * self.CW)
        for i in range(self.TC):
            for j in range(self.TR):
                if self.tiles_list[i][j] != 0:
                    self.tiles_list[i][j].display()

    def control(self, mousex, mousey):
        col = mousex / self.CW
        row = mousey / self.CW
        if self.tiles_list[col][row] == 0:
            color = self.COLOR.pop()
            if color == self.BLACK:
                self.black_count += 1
            else:
                self.white_count += 1
            self.tiles_list[col][row] = Tile(col, row, color, self.CW)
            self.COLOR.insert(0, color)

    def update(self):
        """Carries out necessary actions if pinky or player wins"""
        if self.black_count + self.white_count == 16:
            if self.white_count > self.black_count:
                fill(1)
                textSize(50)
                text("BLACK WINS", 100, 100)
            elif self.white_count < self.black_count:
                fill(1)
                textSize(50)
                text("WHITE WIN!!!", 140, 140)
            else:
                fill(0, 0, 225)
                textSize(50)
                text("The same", 100, 200)  
