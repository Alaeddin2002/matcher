import csv
import random

random.seed(42) 

input_file = "data/annotated-index.tsv"
# train_file = "data/annotated-index-train.tsv"
# test_file = "data/annotated-index-test.tsv"

rows = []
with open(input_file, "r") as f:
    reader = csv.reader(f, delimiter="\t")
    header = next(reader)
    for row in reader:
        rows.append(row)
unique_vals = []
for i in rows:
    unique_vals.append(i[0])
unique_vals = list(set(unique_vals))
random.shuffle(unique_vals)

train_vals = unique_vals[:int(0.8 * len(unique_vals))]
test_vals = unique_vals[int(0.8 * len(unique_vals)):]

train_rows = []
test_rows = []

for row in rows:
    if row[0] in train_vals:
        train_rows.append(row)
    else:
        test_rows.append(row)

train_file = "data/annotated-index-train.tsv"
test_file = "data/annotated-index-test.tsv"

with open(train_file, "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(header)
    writer.writerows(train_rows)

with open(test_file, "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(header)
    writer.writerows(test_rows)
    
print('done')