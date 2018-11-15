import re
class CharFreq:
    def __init__(self):
        self.char_count = {}
        self.char_total = 0

    def add_char(self, char):
        self.char_total += 1
        if char in self.char_count.keys():
            self.char_count[char] += 1
        else:
            self.char_count[char] = 1

    def count_line(self, line):
        chars = re.findall(r"\w", line.lower())
        for c in chars:
            self.add_char(c)