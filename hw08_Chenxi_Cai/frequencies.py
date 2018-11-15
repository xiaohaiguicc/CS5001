"""class to deal with counting frequencies of n-gram"""


class NgramFrequencies:
    def __init__(self):
        self.unigrams_dic = {"COUNT": 0}
        self.bigrams_dic = {"COUNT": 0}
        self.trigrams_dic = {"COUNT": 0}

    def add_item(self, ngram, collection):
        """Given a n-grams and its dictionary,
        increments its count in the dictionary
        String, Dictionary -> None"""
        if ngram in collection.keys():
            collection[ngram] += 1
        else:
            collection[ngram] = 1
        collection["COUNT"] += 1

    def fill_in_dic(self, word_per_list):
        """Given the word list with words in a sentence,
        assign three dictionaries"""
        for word in word_per_list:
            self.add_item(word, self.unigrams_dic)

        for i in range(len(word_per_list) - 1):
            bigrams = word_per_list[i] + "_" + word_per_list[i + 1]
            self.add_item(bigrams, self.bigrams_dic)

        for i in range(len(word_per_list) - 2):
            trigrams = (word_per_list[i] + "_"
                        + word_per_list[i + 1]
                        + "_" + word_per_list[i + 2])
            self.add_item(trigrams, self.trigrams_dic)

    def top_n_counts(self, collection):
        """Given a dictionary, returns a list of items sorted on the count
        Dictionary -> List of tuples"""
        top_count = sorted(
            collection.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return top_count

    def top_n_freq(self, top_count, count):
        """Given a list sorted on the count and the total counts,
        returns a list of items sorted on frequencies
        List, Integer -> List"""
        top_freq = []
        for item in top_count:
            top_freq.append((item[0], self.frequency(item[1], count)))
        return top_freq

    def frequency(self, item, count):
        """Given an item and the total count, return its frequency
        String, Integer -> Float"""
        return item / count

    def top_n_grams(self, collection, range):
        """Given a dicrtionary and range,
        return the top n ngrams
        Dictionary, Integer -> list"""
        count = collection.pop("COUNT")
        top_count = self.top_n_counts(collection)
        top_freq = self.top_n_freq(top_count, count)
        return top_freq[:range]
