from bracket_match import BracketMatch


def test_brackets_match():
    """Test brackets_match method"""
    # Include the following cases in your test:
    # "()" should succeed
    # "a(a[a])a({a})" should succeed
    # "(" should not succeed
    # "(}" should not succeed
    # "a(a(a)a(a)" should not succeed
    # "aa(a))a(a)" should not succeed
    bracket = BracketMatch()
    result = bracket.brackets_match("()")
    assert result is True
    result = bracket.brackets_match("a(a[a])a({a})")
    assert result is True
    result = bracket.brackets_match("(")
    assert result is False
    result = bracket.brackets_match("(}")
    assert result is False
    result = bracket.brackets_match("a(a(a)a(a)")
    assert result is False
    result = bracket.brackets_match("aa(a))a(a)")
    assert result is False
