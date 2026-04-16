## Matcher Project

This project investigates the problem of fuzzy matching. 

Much of words may be similar but get a rating of 0 in exact matching, this project aims to change that, and explore tehniques that rank similar words.

Methods Tested:

* Exact Match
* Jaccard Similarity
* Levenshtein Similarity
* TF-IDF Cosine Similarity

## Dependencies

``` pip install -r requirements.txt ```

## Running 

``` python3 -m matcher.bin.main -f data/annotated-index-test.tsv -s <scorer> -e -t <threshold>```

Arguments:
1. -f / --file: Path to dataset
2. -s / --scorer: One of exact, jaccard, levenshtein, tfidf
3. -e: Evaluate results
4. -t / --threshold

## Testing 

``` python3 -m pytest ```