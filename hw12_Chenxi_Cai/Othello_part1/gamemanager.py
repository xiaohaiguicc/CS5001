from tiles import Tiles
from tile import Tile
import re
# The gamemanager class extends Tiles, so methods defined in Tiles
# are inherited by objects of class GameManager.


class GameManager(Tiles):
    """GameManager class"""
    def __init__(self, TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH):
        Tiles.__init__(self, TOTAL_COLUMN, TOTAL_ROW, CELL_WIDTH)
        self.turn = 0
        self.end = False

    def player_make_move(self,  mousex, mousey):
        """Handles mouse input for tiles"""
        col = mousex // self.CW
        row = mousey // self.CW
        if self.nolegal("BLACK"):
            self.turn = 1
        elif (self.tiles_list[col][row] == 0 and
              self.islegal(col, row, "BLACK", "flip")):
            self.tiles_list[col][row] = Tile(col, row, self.BLACK, self.CW)
            self.turn = 1

    def computer_make_move(self):
        """computer's turn"""
        if self.turn == 1:
            if self.nolegal("WHITE"):
                self.turn = 0
            else:
                maxflip = 0
                for col in range(self.TC):
                    for row in range(self.TR):
                        if self.tiles_list[col][row] == 0:
                            self.computer_flip()
                            if (self.islegal(col, row, "WHITE", "count") and
                               self.flip_count > maxflip):
                                maxflip = self.flip_count
                                computer_col, computer_row = col, row

                self.tiles_list[computer_col][computer_row] = (
                    Tile(computer_col, computer_row, self.WHITE, self.CW))
                self.islegal(computer_col, computer_row, "WHITE", "flip")
                self.turn = 0

    def update(self):
        """Carry out necessary updates before
        drawing to screen"""
        self.black_count = 0
        self.white_count = 0
        for col in range(self.TC):
            for row in range(self.TR):
                if self.tiles_list[col][row] != 0:
                    if self.tiles_list[col][row].color == self.BLACK:
                        self.black_count += 1
                    else:
                        self.white_count += 1
        fill(225, 0, 0)
        textSize(20)
        text("WHITE:" + str(self.white_count), (self.TC - 1) * self.CW, 20)
        text("BLACK:" + str(self.black_count), (self.TR - 1) * self.CW, 40)
        if self.end:
            with open('scores.txt', 'r') as f:
                lines = f.readlines()
                p = re.compile(r'\d+')
            if lines and p.findall(lines[0]):
                max_value = int(p.findall(lines[0])[0])
            else:
                max_value = self.black_count
            name = self.setup()
            if name:
                new_line = name + "\t" + str(self.black_count) + "\n"
                with open('scores.txt', 'w') as f:
                    if self.black_count > max_value:
                        lines.insert(0, new_line)
                    else:
                        lines.append(new_line)
                    for line in lines:
                        f.write(line)
            noLoop()

    def result(self):
        """Carries out necessary actions if computer or player wins"""
        if self.nolegal("WHITE") and self.nolegal("BLACK"):
            self.end = True
        if self.black_count + self.white_count == self.TC * self.TR:
            self.end = True
        if self.end:
            if self.white_count < self.black_count:
                fill(225, 0, 0)
                textSize(50)
                text("BLACK WINS!", (self.TC / 2 - 1) * self.CW,
                     self.TR / 2 * self.CW)
            elif self.white_count > self.black_count:
                fill(225, 0, 0)
                textSize(50)
                text("WHITE WIN!", (self.TC / 2 - 1) * self.CW,
                     self.TR / 2 * self.CW)
            else:
                fill(225, 0, 0)
                textSize(50)
                text("The same!", (self.TC / 2 - 1) * self.CW,
                     self.TR / 2 * self.CW)

    def setup(self):
        """
        prompt the user for their name
        """
        answer = self.input('enter your name')
        return answer

    def input(self, message=''):
        """Processing Python """
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
