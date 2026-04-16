import abc
import csv
import collections.abc
import dataclasses
from matcher.name_matcher import NameMatchScorer


@dataclasses.dataclass
class Comparison:
    """Class representing two names, their similarity score, and the true label."""
    name1: str
    name2: str
    score: float = 0.0
    label: int = 0


class DocIterator(abc.ABC, collections.abc.Iterator):
    def __str__(self):
        return self.__class__.__name__


class TsvIterator(DocIterator):
    """Iterator to iterate over tsv-formatted documents."""
    def __init__(self, path, scorer=NameMatchScorer):
        self.path = path
        self.scorer = scorer
        self.fp = open(self.path, "r", encoding="utf-8")
        self.reader = csv.reader(self.fp, delimiter="\t")
        next(self.reader)  # skip header row

    def __iter__(self):
        return self

    def __next__(self):
        try:
            row = next(self.reader)
            name1 = row[0]
            name2 = row[1]
            label = int(row[2])

            scorer = self.scorer(name1, name2)
            score = scorer.score(name1, name2)

            return Comparison(name1, name2, score, label)

        except StopIteration:
            self.fp.close()
            raise