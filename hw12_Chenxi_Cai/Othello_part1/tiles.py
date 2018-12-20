from tile import Tile


class Tiles:
    """A collection of tiles"""
    def __init__(self, TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH):
        self.TC = TOTAL_COLUMN
        self.TR = TOTAL_ROW
        self.CW = CELL_WIDTH
        self.WHITE = 225
        self.BLACK = 0
        self.white_count = 2
        self.black_count = 2
        self.flip_count = 0
        self.tiles_list = [[0] * self.TR for i in range(self.TC)]
        self.tiles_list[self.TC // 2 - 1][self.TR // 2 - 1] = Tile(
            self.TC // 2 - 1, self.TR // 2 - 1, self.WHITE, self.CW)
        self.tiles_list[self.TC // 2][self.TR // 2] = Tile(
            self.TC // 2, self.TR // 2, self.WHITE, self.CW)
        self.tiles_list[self.TC // 2][self.TR // 2 - 1] = Tile(
            self.TC // 2, self.TR // 2 - 1, self.BLACK, self.CW)
        self.tiles_list[self.TC // 2 - 1][self.TR // 2] = Tile(
            self.TC // 2 - 1, self.TR // 2, self.BLACK, self.CW)

    def display(self):
        """Display tiles"""
        for i in range(self.TC):
            for j in range(self.TR):
                if self.tiles_list[i][j] != 0:
                    self.tiles_list[i][j].display()
        self.update()

    def islegal(self, col, row, colorstr, action):
        """
        Recognize a legal/illegal move of a color
        and then flip tiles or count how many tiles can be flipped.
        Argument:
        col, row is tile's position,
        colorstr is tile's color, player-black, computer-white
        action: "flip" or "count"
        "flip" means flip tiles;
        "count" means count the total tiles can be flipped;
        int, int, string, string -> return boolean
        """
        if colorstr == "BLACK":
            color = self.BLACK
            color_oppo = self.WHITE
        elif colorstr == "WHITE":
            color = self.WHITE
            color_oppo = self.BLACK

        legal = False
        # 1. same col, top
        if row != 0:
            tile = self.tiles_list[col][row - 1]
            if tile != 0 and tile.color == color_oppo:
                for i in range(row - 1, -1, -1):
                    if self.tiles_list[col][i] == 0:
                        break
                    elif self.tiles_list[col][i].color == color:
                        if action == "flip":
                            self.flipping(i + 1, row, "col", color, col)
                        elif action == "count":
                            self.flip_count += row - i - 1
                        legal = True
                        break
        # 2. same col, bottom
        if row != self.TR - 1:
            tile = self.tiles_list[col][row + 1]
            if tile != 0 and tile.color == color_oppo:
                for i in range(row + 1, self.TR):
                    if self.tiles_list[col][i] == 0:
                        break
                    elif self.tiles_list[col][i].color == color:
                        if action == "flip":
                            self.flipping(row + 1, i, "col", color, col)
                        elif action == "count":
                            self.flip_count += i - row - 1
                        legal = True
                        break
        # 3. same row, left
        if col != 0:
            tile = self.tiles_list[col - 1][row]
            if tile != 0 and tile.color == color_oppo:
                for i in range(col - 1, -1, -1):
                    if self.tiles_list[i][row] == 0:
                        break
                    elif self.tiles_list[i][row].color == color:
                        if action == "flip":
                            self.flipping(i + 1, col, "row", color, row)
                        elif action == "count":
                            self.flip_count += col - i - 1
                        legal = True
                        break
        # 4. same row, right
        if col != self.TC - 1:
            tile = self.tiles_list[col + 1][row]
            if tile != 0 and tile.color == color_oppo:
                for i in range(col + 1, self.TC):
                    if self.tiles_list[i][row] == 0:
                        break
                    elif self.tiles_list[i][row].color == color:
                        if action == "flip":
                            self.flipping(col + 1, i, "row", color, row)
                        elif action == "count":
                            self.flip_count += i - col - 1
                        legal = True
                        break
        # 5. left top
        if row != 0 and col != 0:
            tile = self.tiles_list[col - 1][row - 1]
            if tile != 0 and tile.color == color_oppo:
                for i in range(1, min(row, col) + 1):
                    if self.tiles_list[col - i][row - i] == 0:
                        break
                    elif self.tiles_list[col - i][row - i].color == color:
                        if action == "flip":
                            self.flipping(1, i, "leftdiag", color,
                                          col - i, row - i)
                        elif action == "count":
                            self.flip_count += i - 1
                        legal = True
                        break
        # 6. right bottom
        if row != self.TR - 1 and col != self.TC - 1:
            tile = self.tiles_list[col + 1][row + 1]
            if tile != 0 and tile.color == color_oppo:
                for i in range(1, min(self.TR - row, self.TC - col)):
                    if self.tiles_list[col + i][row + i] == 0:
                        break
                    elif self.tiles_list[col + i][row + i].color == color:
                        if action == "flip":
                            self.flipping(1, i, "leftdiag", color, col, row)
                        elif action == "count":
                            self.flip_count += i - 1
                        legal = True
                        break
        # 7. right top
        if row != 0 and col != self.TC - 1:
            tile = self.tiles_list[col + 1][row - 1]
            if tile != 0 and tile.color == color_oppo:
                for i in range(1, min(row + 1, self.TC - col)):
                    if self.tiles_list[col + i][row - i] == 0:
                        break
                    elif self.tiles_list[col + i][row - i].color == color:
                        if action == "flip":
                            self.flipping(1, i, "rightdiag", color, col, row)
                        elif action == "count":
                            self.flip_count += i - 1
                        legal = True
                        break
        # 8. left bottom
        if row != self.TR - 1 and col != 0:
            tile = self.tiles_list[col - 1][row + 1]
            if tile != 0 and tile.color == color_oppo:
                for i in range(1, min(col + 1, self.TR - row)):
                    if self.tiles_list[col - i][row + i] == 0:
                        break
                    elif self.tiles_list[col - i][row + i].color == color:
                        if action == "flip":
                            self.flipping(1, i, "rightdiag", color,
                                          col - i, row + i)
                        elif action == "count":
                            self.flip_count += i - 1
                        legal = True
                        break
        return legal

    def flipping(self, start, end, position, color, axis, axis2=0):
        """flipping tiles from start place to end place(exclude end)
            position is the unchanged asix and axis is the value of axis,
            axis2 is used for diagonal case.
            color is the new color of flipped tiles
            input: int, int, string, color, int, int
        """
        if position == "col":
            for i in range(start, end):
                self.tiles_list[axis][i].color = color
        if position == "row":
            for i in range(start, end):
                self.tiles_list[i][axis].color = color
        if position == "leftdiag":
            for i in range(start, end):
                self.tiles_list[axis + i][axis2 + i].color = color
        if position == "rightdiag":
            for i in range(start, end):
                self.tiles_list[axis + i][axis2 - i].color = color

    def nolegal(self, color):
        """check if there are no more legal moves
        color is string
        """
        for col in range(self.TC):
            for row in range(self.TR):
                if self.tiles_list[col][row] == 0:
                    if self.islegal(col, row, color, "count"):
                        return False
        return True

    def computer_flip(self):
        """reset flip count value"""
        self.flip_count = 0
