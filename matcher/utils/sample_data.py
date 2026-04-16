import csv
import random

random.seed(42)  

input_file = "data/annotated-index-test.tsv"
output_file = "data/annotated-index-test-sampled.tsv"

rows = []

with open(input_file, "r") as f:
    reader = csv.reader(f, delimiter="\t")
    header = next(reader)
    for row in reader:
        rows.append(row)


sample_size = int(0.1 * len(rows))
sampled_rows = random.sample(rows, sample_size)

with open(output_file, "w") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(header)
    writer.writerows(sampled_rows)

print(f"Saved {sample_size} rows to {output_file}")