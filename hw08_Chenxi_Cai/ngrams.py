"""calculate n0grams frequencies"""
import sys
from text_cleaner import TextCleaner
from frequencies import NgramFrequencies


def main(file_name):
    """Given the file name, print n-grams frequencies
    String -> None"""
    text = TextCleaner()
    ngrams = NgramFrequencies()
    text.read_file(file_name)
    for i in range(0, len(text.lines)):
        text.pre_process(text.lines[i])

    for word_per_list in text.word_list:
        ngrams.fill_in_dic(word_per_list)

    ngrams_list = [
        ngrams.unigrams_dic,
        ngrams.bigrams_dic,
        ngrams.trigrams_dic
        ]
    ngrams_name_list = ["unigrams", "bigrams", "trigrams"]
    for i in range(3):
        grams_top = ngrams.top_n_grams(ngrams_list[i], 10)
        print_output(grams_top, ngrams_name_list[0])


def print_output(ngrams_list, ngrams_name):
    print("Top 10", ngrams_name + ":")
    for item in ngrams_list:
        # new_item = (item[0], round(item[1], 3))
        print("\t", item)


main(sys.argv[1])
