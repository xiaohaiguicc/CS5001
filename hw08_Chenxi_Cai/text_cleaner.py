"""class to deal with text pre-processing """
import re


class TextCleaner:
    def __init__(self):
        """Constructor
        initialize a list contains all lines in file
        and a list whose item is a list of words in each sentence"""
        self.lines = []
        self.word_list = []

    def read_file(self, file_name):
        """Given the file's name, open it and assign all lines to list
        string -> None"""
        try:
            with open(file_name) as f:
                self.lines = f.readlines()
        except FileNotFoundError:
            print("Can't open", file_name)
            return

    def lowercase(self, line):
        """Given a line and return it with lowercase characters
        String -> String"""
        return line.lower()

    def replace_char(self, line):
        """Given a line and replace mr., dr., "," to mrdot, drdot and COMMA
        String -> String"""
        if "mr." in line:
            line = line.replace("mr.", "mrdot")
        if "dr." in line:
            line = line.replace("dr.", "drdot")
        line = line.replace(",", " COMMA")
        return line

    def sentence(self, line):
        """Given a line and return sentences in this line
        String -> list"""
        sentence_list = line.split(".")
        return sentence_list

    def words(self, sentence):
        """Given a sentence and return words in it
        String -> list"""
        word_list = re.findall(r"\w+\'s|\w+\-\w+|\w+", sentence)
        return word_list

    def pre_process(self, line):
        """Given a line, deal it with all pre processing
        assign word list with a list of words in axs sentence
        String -> list"""
        line = self.lowercase(line)
        line = self.replace_char(line)
        sentence_list = self.sentence(line)
        for sentence in sentence_list:
            self.word_list.append(self.words(sentence))
