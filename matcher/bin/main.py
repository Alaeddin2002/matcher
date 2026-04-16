import argparse
from matcher.name_matcher import ExactMatchScorer, JaccardScorer, LevenshteinScorer, TfidfMatcher
from matcher.utils.parse_tsv import TsvIterator
from matcher.eval.eval import evaluate
import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_scorer(scorer_name):
    scorer_name = scorer_name.lower()
    if scorer_name == 'exact':
        return ExactMatchScorer
    elif scorer_name == 'jaccard':
        return JaccardScorer
    elif scorer_name == 'levenshtein':
        return LevenshteinScorer
    elif scorer_name == 'tfidf':
        return TfidfMatcher
    else:
        raise ValueError(f"Unknown scorer name: {scorer_name}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate name matching algorithms")
    parser.add_argument('-f', '--file', type=str, required=True,
                        help='TSV file containing name pairs and true labels')
    parser.add_argument('-s', '--scorer', required=True,
                        choices=["exact", "jaccard", "levenshtein", "tfidf"],
                        help='Name matching algorithm to use')
    parser.add_argument('-p', '--print_results', action='store_true',
                        help='Whether to print results to console')
    parser.add_argument('-e', '--evaluate', action='store_true',
                        help='Whether to evaluate results')
    parser.add_argument('-t', '--threshold', type=float, default=0.5,
                        help='Threshold for predicting a match')
    args = parser.parse_args()

    scorer_class = get_scorer(args.scorer)
    iterator = TsvIterator(args.file, scorer_class)

    logging.info(f"Starting scoring with scorer={args.scorer}, threshold={args.threshold}, file={args.file}")

    results = []

    for comparison in iterator:
        predicted_label = 1 if comparison.score >= args.threshold else 0

        results.append({
            'name1': comparison.name1,
            'name2': comparison.name2,
            'score': comparison.score,
            'true_label': comparison.label,
            'predicted_label': predicted_label,
        })

        if len(results) % 500 == 0:
            logging.info(f"Scored {len(results)} pairs so far...")

    logging.info(f"Finished scoring {len(results)} pairs total.")

    if args.print_results:
        for result in results[:20]:
            print(result)

    if args.evaluate:
        logging.info("Evaluating results...")
        f1_results = evaluate(results, 'f1')
        accuracy_results = evaluate(results, 'accuracy')
        precision_results = evaluate(results, 'precision')
        recall_results = evaluate(results, 'recall')
        logging.info(f"Evaluation complete — F1={f1_results:.4f}, Precision={precision_results:.4f}, Recall={recall_results:.4f}")

        print(f"Evaluation results (F1): {f1_results}")
        print(f"Evaluation results (Accuracy): {accuracy_results}")
        print(f"Evaluation results (Precision): {precision_results}")
        print(f"Evaluation results (Recall): {recall_results}")


if __name__ == "__main__":
    main()