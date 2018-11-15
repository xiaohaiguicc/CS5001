"""PyTest test suite for NgramFrequencies class"""

from frequencies import NgramFrequencies


def test_constructor():
    """test the constructor"""
    ngrams = NgramFrequencies()
    assert ngrams.unigrams_dic["COUNT"] == 0
    assert ngrams.bigrams_dic["COUNT"] == 0
    assert ngrams.trigrams_dic["COUNT"] == 0


def test_add_items():
    """test adding a n-gram"""
    ngrams = NgramFrequencies()
    assert "the" not in ngrams.unigrams_dic
    ngrams.add_item("the", ngrams.unigrams_dic)
    assert ngrams.unigrams_dic["the"] == 1
    ngrams.add_item("the", ngrams.unigrams_dic)
    assert ngrams.unigrams_dic["the"] == 2
    assert ngrams.unigrams_dic["COUNT"] == 2


def test_fill_in_dic():
    """test filling in three dictionary"""
    ngrams = NgramFrequencies()
    word_per_list = ["time", "burton's", "corpse", "bride"]
    ngrams.fill_in_dic(word_per_list)
    assert ngrams.unigrams_dic == {
        "COUNT": 4,
        "time": 1,
        "burton's": 1,
        "corpse": 1,
        "bride": 1
    }
    assert ngrams.bigrams_dic == {
        "COUNT": 3,
        "time_burton's": 1,
        "burton's_corpse": 1,
        "corpse_bride": 1
    }
    assert ngrams.trigrams_dic == {
        "COUNT": 2,
        "time_burton's_corpse": 1,
        "burton's_corpse_bride": 1
    }


def test_top_n_counts():
    """test returning a list of items sorted on the count"""
    ngrams = NgramFrequencies()
    new_dic = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    top_list = ngrams.top_n_counts(new_dic)
    assert top_list == [("d", 4), ("c", 3), ("b", 2), ("a", 1)]


def test_top_n_freqs():
    """test returning a list of items sorted on the frequencies"""
    ngrams = NgramFrequencies()
    top_list = [("d", 4), ("c", 3), ("b", 2), ("a", 1)]
    top_freq = ngrams.top_n_freq(top_list, 10)
    assert top_freq == [("d", 0.4), ("c", 0.3), ("b", 0.2), ("a", 0.1)]


def test_frequency():
    """test frequency calculation"""
    ngrams = NgramFrequencies()
    freq = ngrams.frequency(2, 10)
    assert freq == 0.2


def test_top_n_grams():
    """test final top n list"""
    ngrams = NgramFrequencies()
    unigrams_dic = {
        "COUNT": 10,
        "time_burton's": 5,
        "burton's_corpse": 4,
        "corpse_bride": 1
    }
    top_n_unigrams = ngrams.top_n_grams(unigrams_dic, 2)
    assert top_n_unigrams == [
        ("time_burton's", 0.5),
        ("burton's_corpse", 0.4)
    ]
