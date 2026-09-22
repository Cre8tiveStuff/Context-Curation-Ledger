from ccl import count_tokens
from ccl import fit_to_budget

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

def test_fit_budget_stops_at_limit():
    chunks = ["word " * 100 for _ in range (5)]
    result = fit_to_budget(chunks, max_tokens=250)
    assert len(result) == 2 

def test_fit_to_budget_keeps_all_under_budget():
    chunks = ["short_chunk"] * 3
    result = fit_to_budget(chunks, max_tokens=1000)
    assert len(result) == 3 
