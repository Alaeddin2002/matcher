from Levenshtein import distance
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class NameMatchScorer:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def __str__(self):
        return f"{self.__class__.__name__}(name1='{self.name1}', name2='{self.name2}')"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name1}', '{self.name2}')"

    def score(self, name1, name2):
        raise NotImplementedError("Subclasses must implement score().")


class ExactMatchScorer(NameMatchScorer):
    def score(self, name1, name2):
        return 1.0 if name1.strip().lower() == name2.strip().lower() else 0.0


class JaccardScorer(NameMatchScorer):
    def score(self, name1, name2):
        set1 = set(name1.strip().lower())
        set2 = set(name2.strip().lower())

        union = set1.union(set2)
        if not union:
            return 0.0

        intersection = set1.intersection(set2)
        return len(intersection) / len(union)


class LevenshteinScorer(NameMatchScorer):
    def score(self, name1, name2):
        name1 = name1.strip().lower()
        name2 = name2.strip().lower()

        max_len = max(len(name1), len(name2))
        if max_len == 0:
            return 1.0

        lev_distance = distance(name1, name2)
        return 1 - (lev_distance / max_len)


class TfidfMatcher(NameMatchScorer):
    def __init__(self, name1, name2, ngram_range=(1, 4)):
        super().__init__(name1, name2)

        if not isinstance(ngram_range, tuple) or len(ngram_range) != 2:
            raise ValueError("ngram_range must be a tuple of length 2")
        if ngram_range[0] < 1 or ngram_range[1] < ngram_range[0]:
            raise ValueError("Invalid ngram_range values")

        self.ngram_range = ngram_range

    def score(self, name1, name2):
        vectorizer = TfidfVectorizer(
            analyzer="char",
            ngram_range=self.ngram_range
        )

        tfidf_matrix = vectorizer.fit_transform(
            [name1.strip().lower(), name2.strip().lower()]
        )

        return cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]