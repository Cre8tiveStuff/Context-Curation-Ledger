from ccl import count_tokens

def test_count_tokens_returns_positive_int():
    result = count_tokens("This is a test sentence.")
    assert isinstance(result, int)
    assert result > 0

def test_count_tokens_empty_string_is_zero():
    assert count_tokens("") == 0

def test_count_tokens_longer_text_has_more_tokens():
    short = count_tokens("Short text.")
    long = count_tokens("This is a considerably longer piece of text with many more words in it.")
    assert long > short