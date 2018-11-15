# It is a test file. line the command line, write "pytest" to test cases

from character_freq import CharFreq


def test_constructor():
    """test the constructor"""
    char_freqs = CharFreq()
    assert char_freqs.char_total == 0
    assert char_freqs.char_count == {} # assert用来判断后面是不是真的，不是就失败，是就pass
    

def test_add_char():
    """Test adding a character to the count"""
    char_freq = CharFreq()
    assert "a" not in char_freq.char_count
    char_freq.add_char("a")
    assert char_freq.char_count["a"] == 1
    char_freq.add_char("a")
    assert char_freq.char_count["a"] == 2

def test_count_line():
    char_feq = CharFreq()
    char_feq.count_line("abA")
    assert char_feq.char_count["a"] == 2
    assert char_feq.char_count["b"] == 1
