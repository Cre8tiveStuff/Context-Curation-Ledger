from ccl import count_tokens
from ccl import fit_to_budget
from ccl import position_aware_order
from comparison_log import log_comparison, get_comparisons

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
    chunks = ["word " * 100 for _ in range(5)]
    result = fit_to_budget(chunks, max_tokens=250)
    assert len(result) == 2

def test_fit_to_budget_keeps_all_under_budget():
    chunks = ["short_chunk"] * 3
    result = fit_to_budget(chunks, max_tokens=1000)
    assert len(result) == 3

def test_position_aware_order_puts_top_chunk_first():
    ranked = ["best", "second", "third", "fourth", "worst"]
    result = position_aware_order(ranked)
    assert result[0] == "best"

def test_position_aware_order_puts_second_chunk_last():
    ranked = ["best", "second", "third", "fourth", "worst"]
    result = position_aware_order(ranked)
    assert result[-1] == "second"

def test_position_aware_order_short_list_unchanged():
    ranked = ["only_one"]
    result = position_aware_order(ranked)
    assert result == ["only_one"]

def test_log_comparison_stores_and_retrieves():
    log_comparison(
        question="Test question?",
        baseline_answer="Baseline answer.",
        baseline_score=70.0,
        curated_answer="Curated answer.",
        curated_score=90.0
    )
    results = get_comparisons()
    assert len(results) >= 1
    assert results[-1][0] == "Test question?"
    assert results[-1][2] == 90.0