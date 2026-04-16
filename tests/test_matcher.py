import csv
import os
import pytest
from matcher.name_matcher import ExactMatchScorer, JaccardScorer, LevenshteinScorer, TfidfMatcher

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "test_names.tsv")


def load_test_names():
    """Load name pairs and expected match labels from test_names.tsv."""
    pairs = []
    with open(DATA_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            pairs.append((row["name1"], row["name2"], int(row["match"])))
    return pairs



def test_exact_match_identical():
    scorer = ExactMatchScorer("Alice", "alice")
    assert scorer.score("Alice", "alice") == 1.0


def test_exact_match_different():
    scorer = ExactMatchScorer("Alice", "Bob")
    assert scorer.score("Alice", "Bob") == 0.0


def test_exact_match_from_file():
    for name1, name2, match in load_test_names():
        scorer = ExactMatchScorer(name1, name2)
        result = scorer.score(name1, name2)
        if match == 1 and name1.strip().lower() == name2.strip().lower():
            assert result == 1.0
        elif name1.strip().lower() != name2.strip().lower():
            assert result == 0.0


def test_jaccard_similar_names():
    scorer = JaccardScorer("Alice", "Alicia")
    assert scorer.score("Alice", "Alicia") > 0.0


def test_jaccard_identical():
    scorer = JaccardScorer("John", "John")
    assert scorer.score("John", "John") == 1.0


def test_jaccard_no_overlap():
    scorer = JaccardScorer("xyz", "qwv")
    assert scorer.score("xyz", "qwv") == 0.0



def test_levenshtein_similar_names():
    scorer = LevenshteinScorer("Alice", "Alicia")
    assert 0.0 < scorer.score("Alice", "Alicia") < 1.0


def test_levenshtein_identical():
    scorer = LevenshteinScorer("John", "John")
    assert scorer.score("John", "John") == 1.0


def test_levenshtein_very_different():
    scorer = LevenshteinScorer("Alice", "Bob")
    assert scorer.score("Alice", "Bob") < 0.5



def test_tfidf_similar_names():
    scorer = TfidfMatcher("Alice", "Alicia")
    assert scorer.score("Alice", "Alicia") > 0.0


def test_tfidf_identical():
    scorer = TfidfMatcher("John", "John")
    assert scorer.score("John", "John") == pytest.approx(1.0, abs=1e-6)


def test_tfidf_invalid_ngram_range_reversed():
    with pytest.raises(ValueError):
        TfidfMatcher("Alice", "Bob", ngram_range=(4, 1))


def test_tfidf_invalid_ngram_range_zero():
    with pytest.raises(ValueError):
        TfidfMatcher("Alice", "Bob", ngram_range=(0, 3))


def test_tfidf_invalid_ngram_range_not_tuple():
    with pytest.raises(ValueError):
        TfidfMatcher("Alice", "Bob", ngram_range=[1, 4])