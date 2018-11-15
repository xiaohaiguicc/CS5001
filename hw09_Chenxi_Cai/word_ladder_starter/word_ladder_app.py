from word_ladder import WordLadder


def main():
    """Run an interactive command line to let the user
    input word pairs and generate word ladders"""
    english_words = load_words()

    while True:
        w1, w2 = input("> ").split()
        worddic = word_dic(w1, w2, english_words)
        # Create a WordLadder object
        wl = WordLadder(w1, w2, worddic)
        # Generate the word ladder
        word_ladder = wl.make_ladder()
        print("Ladder: ", word_ladder)


def load_words():
    """Load words from complete wordlist file"""
    # We're creating a dictionary keyed on word
    # length, so that we can quickly get to a set of
    # words of a given length.
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words


def word_dic(w1, w2, valid_word):
    """Return dictionary with words from len(w1) to len(w2)
    from the whole word dictionary.
    Integer, Integer, Dictionary -> Dictionary"""
    worddic = {}
    if len(w1) <= len(w2):
        len_s = len(w1)
        len_l = len(w2)
    else:
        len_s = len(w2)
        len_l = len(w1)
    for i in range(len_s, len_l + 1):
        worddic[i] = valid_word[i]
    return worddic

main()
