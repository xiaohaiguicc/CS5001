import re


class DataAnalysis:

    def __init__(self, file):
        """Given file name, set up some instance variables
        string -> Nnoe"""
        # TODO: set up the necessary instance variables
        self.lang_collection = {}
        self.country_collection = {}
        self.peple_count = 0
        self.read_data(file)

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        """Given file name, assign values to lists and integer
           of the class.
           string -> None"""
        try:
            with open(file_name) as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Can't open", file_name)
            return
        for line in lines[1:]:
            line_list = re.split(r"[,\n]", line)
            lang = line_list[6]

            self.add_key(self.lang_collection, lang)
            country = re.findall(r'\.([a-z].)$', line_list[3])
            if len(country) != 0:
                self.add_key(self.country_collection, country[0])
            self.peple_count += 1

    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.
    def top_n_lang_freqs(self, length):
        """Given a number, return N-length list of tuples
        Integer -> list of tuples"""
        lang_by_freq = self.change_to_freq(
            self.lang_collection, self.peple_count)
        lang_by_count = sorted(
            lang_by_freq.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return lang_by_count[:length]

    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered
    # from highest frequency to lowest.
    def top_n_country_tlds_freqs(self, length):
        """Given a number, return N-length list of tuples
        representing country and their frequencies
        Integer -> list of tuples"""
        country_by_freq = self.change_to_freq(
            self.country_collection, self.peple_count)
        country_by_count = sorted(
            country_by_freq.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return country_by_count[:length]

    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.
    def add_key(self, collection, key):
        """Given a dictionary and keys, return dictionary
        whose values is the count of keys.
           dictionary, string -> dictionary"""
        if key in collection.keys():
            collection[key] += 1
        else:
            collection[key] = 1

    def change_to_freq(self, collection, length):
        """Given dictionary and a number N, return a new dictionary
        whose values = original values / N
        dictionary, Integer -> dictionary"""
        for key in collection.keys():
            collection[key] = collection[key] / length
        return collection
