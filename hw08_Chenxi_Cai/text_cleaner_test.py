"""PyTest test suite for TextCleaner class"""
from text_cleaner import TextCleaner


def test_constructor():
    """test the constructor"""
    text = TextCleaner()
    assert text.lines == []
    assert text.word_list == []


def test_read_file():
    """test opening file"""
    text = TextCleaner()
    text.read_file("corpse_bride.txt")
    assert text.lines != []


def test_lowercase():
    """test changing all characters to lowercase"""
    text = TextCleaner()
    line = "AndjcAjd"
    line = text.lowercase(line)
    assert line == "andjcajd"


def test_replace_char():
    """test replacing mr., dr., and ,"""
    text = TextCleaner()
    line = "mr. liu is also dr. liu, we respect him"
    line = text.replace_char(line)
    assert line == "mrdot liu is also drdot liu COMMA we respect him"


def test_sentence():
    """test splitting a paragraph into sentence"""
    text = TextCleaner()
    line = "we are align students. we are fall students"
    sentence_list = text.sentence(line)
    assert sentence_list == ["we are align students", " we are fall students"]


def test_words():
    """test spliting a sentence into words"""
    text = TextCleaner()
    sentence = "a necro philiac \"tim burton's corpse bride\""
    word_list = text.words(sentence)
    assert word_list == ['a', 'necro', 'philiac',
                         'tim', "burton's", 'corpse', 'bride']


def test_pre_process():
    """test all preprocess"""
    text = TextCleaner()
    line = "\"Tim Burton's Corpse Bride\". Marks the Dr. Liu latest, venture."
    text.pre_process(line)
    assert text.word_list == [
        ["tim", "burton's", "corpse", "bride"],
        ["marks", "the", "drdot", "liu", "latest", "COMMA", "venture"],
        []
    ]
