from word_ladder import WordLadder


# TODO: Write appropriate unit tests

def test_make_ladder():
    word_list = load_words("cat", "hat")
    ladder = WordLadder("cat", "hat", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["cat", "hat"]
    word_list = load_words("love", "hate")
    ladder = WordLadder("love", "hate", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["love", "hove", "have", "hate"]
    word_list = load_words("angel", "devil")
    ladder = WordLadder("angel", "devil", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["angel", "anger", "aeger",
                                 "leger", "lever", "level", "devel", "devil"]
    word_list = load_words("earth", "ocean")
    ladder = WordLadder("earth", "ocean", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["earth", "barth", "barih", "baris",
                                 "batis", "bitis", "aitis", "antis",
                                 "antas", "antal", "ontal", "octal",
                                 "octan", "ocean"]
    # Different length test cases
    word_list = load_words("cat", "five")
    ladder = WordLadder("cat", "five", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["cat", "fat", "fit", "fie", "five"]
    word_list = load_words("five", "cat")
    ladder = WordLadder("five", "cat", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["five", "cive", "cave", "cate", "cat"]
    word_list = load_words("dog", "puppy")
    ladder = WordLadder("dog", "puppy", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["dog", "cog", "cop",
                                 "copy", "coppy", "poppy", "puppy"]
    word_list = load_words("sad", "happy")
    ladder = WordLadder("sad", "happy", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["sad", "gad", "gap",
                                 "gapy", "gappy", "happy"]
    word_list = load_words("red", "yellow")
    ladder = WordLadder("red", "yellow", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["red", "bed", "bel",
                                 "bell", "bello", "bellow", "yellow"]
    word_list = load_words("command", "line")
    ladder = WordLadder("command", "line", word_list)
    word_ladder = ladder.make_ladder()
    assert word_ladder.items == ["command", "commend", "compend", "comped",
                                 "coped", "loped", "lope", "lone", "line"]


def load_words(w1, w2):
    """First, Load words from complete wordlist file
    Then return dictionary with words from len(w1) to len(w2)
    from the whole word dictionary.
    Integer, Integer, Dictionary -> Dictionary"""
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    worddic = {}
    if len(w1) <= len(w2):
        len_s = len(w1)
        len_l = len(w2)
    else:
        len_s = len(w2)
        len_l = len(w1)
    for i in range(len_s, len_l + 1):
        worddic[i] = valid_words[i]
    return worddic


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
