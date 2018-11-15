""" Luhn's algorithm"""


class Idnumber:
    """identification numbers"""
    def __init__(self, sequence):
        """constructor, sequence is a string"""
        self.id_list_reverse = [int(item) for item in reversed(sequence)]

    def judge(self):
        """overall procedure"""
        self.double()
        self.modulu()

    def double(self):
        """double value and add them"""
        for i in range(1, len(self.id_list_reverse), 2):
            new_num = self.id_list_reverse[i] * 2
            self.id_list_reverse[i] = new_num // 10 + new_num % 10

    def modulu(self):
        """whether resulting sum is divisible by 10"""
        result = sum(self.id_list_reverse)
        if result % 10 == 0:
            print("The sequence is valid")
        else:
            print("The sequence is not valid")
