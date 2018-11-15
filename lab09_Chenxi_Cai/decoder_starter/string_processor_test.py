from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    # Include the following cases
    # "ab" should yield "" as ouptut
    # "ab*" should yield "b" as output
    # "ab^" should yield "ba" as output
    # "^" should yield "" as output
    string = StringProcessor()
    result = string.process_string("ab")
    assert result == ""
    result = string.process_string("ab*")
    assert result == "b"
    result = string.process_string("ab^")
    assert result == "ba"
    result = string.process_string("^")
    assert result == ""
