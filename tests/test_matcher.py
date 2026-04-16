import pytest
from matcher.name_matcher import ExactMatchScorer, JaccardScorer, LevenshteinScorer, TfidfMatcher

def test_exact_match_scorer():
    scorer = ExactMatchScorer("Alice", "alice")
    assert scorer.score("Alice", "alice") == 1.0
    assert scorer.score("Alice", "Bob") == 0.0
def test_jaccard_scorer():
    scorer = JaccardScorer("Alice", "Alicia")
    assert scorer.score("Alice", "Alicia") > 0.0
    assert scorer.score("Alice", "Bob") == 0.0

def test_levenshtein_scorer():
    scorer = LevenshteinScorer("Alice", "Alicia")
    assert scorer.score("Alice", "Alicia") > 0.0
    assert scorer.score("Alice", "Bob") == 0.0

def test_tfidf_matcher():
    scorer = TfidfMatcher("Alice", "Alicia")
    assert scorer.score("Alice", "Alicia") > 0.0
    assert scorer.score("Alice", "Bob") == 0.0
    