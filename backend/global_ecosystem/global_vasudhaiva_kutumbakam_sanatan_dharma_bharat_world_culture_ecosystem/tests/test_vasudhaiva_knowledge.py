"""Tests for the evidence-aware Vasudhaiva Kutumbakam knowledge base."""
from ..knowledge import (
    answer_historical_question,
    get_complete_knowledge,
    get_core_idea,
    get_primary_text,
    search_knowledge,
)

def test_core_meaning_and_sanskrit_are_available():
    core = get_core_idea()
    assert core["sanskrit"] == "वसुधैव कुटुम्बकम्"
    assert "one family" in core["concise_translation"]

def test_primary_text_identifies_maha_upanishad_and_context():
    text = get_primary_text()
    assert text["work"] == "Mahā Upaniṣad (also written Mahopaniṣad)"
    assert "अयं बन्धुरयं नेति" in text["sanskrit_devanagari"]
    assert "numbering" in text["numbering_note"]

def test_unknown_author_date_and_place_are_not_invented():
    data = get_complete_knowledge()["historical_questions"]
    assert "No historically verified individual author" in data["who_was_it_authored"]["answer"] if "who_was_it_authored" in data else "No historically verified individual author" in data["who_created_or_authored_it"]["answer"]
    assert "not securely known" in data["when_was_it_composed"]["answer"]
    assert "not been established" in data["where_was_it_composed"]["answer"]

def test_search_returns_historical_answer():
    results = search_knowledge("precise place")
    assert results
    assert results[0]["topic"] == "where_was_it_composed"

def test_unknown_question_is_rejected():
    try:
        answer_historical_question("invented_fact")
    except KeyError:
        pass
    else:
        raise AssertionError("Unknown question should raise KeyError")
