## Training Data 

### Exact

Evaluation results (F1): 0.14342629482071714
Evaluation results (Accuracy): 0.9996774998387499
Evaluation results (Precision): 1.0
Evaluation results (Recall): 0.07725321888412018

### Jaccard (Threshhold 0.5)
Evaluation results (F1): 0.5265265265265265
Evaluation results (Accuracy): 0.99976349988175
Evaluation results (Precision): 0.8766666666666667
Evaluation results (Recall): 0.37625178826895567

### Levenshtein (Threshold 0.5)

Evaluation results (F1): 0.2656307806141324
Evaluation results (Accuracy): 0.9990074995037498
Evaluation results (Precision): 0.17914171656686625
Evaluation results (Recall): 0.5135908440629471

## Testing Data 

### Exact

Evaluation results (F1): 0.14857142857142858
Evaluation results (Accuracy): 0.999702
Evaluation results (Precision): 1.0
Evaluation results (Recall): 0.08024691358024691

### Jaccard (Threshold 0.9)

Evaluation results (F1): 0.24107142857142858
Evaluation results (Accuracy): 0.99966
Evaluation results (Precision): 0.43548387096774194
Evaluation results (Recall): 0.16666666666666666

### Jaccard (Threshold 0.5)

Evaluation results (F1): 0.5130434782608696
Evaluation results (Accuracy): 0.999776
Evaluation results (Precision): 0.8676470588235294
Evaluation results (Recall): 0.36419753086419754

### Jaccard (Threshold 0.1)

Evaluation results (F1): 0.0006458019824902368
Evaluation results (Accuracy): 0.015814
Evaluation results (Precision): 0.00032300725852160
Evaluation results (Recall): 0.9814814814814815

### Levenshtein (Threshold 0.9)

Evaluation results (F1): 0.2391304347826087
Evaluation results (Accuracy): 0.99972
Evaluation results (Precision): 1.0
Evaluation results (Recall): 0.13580246913580246

### Levenshtein (Threshold 0.5)

Evaluation results (F1): 0.26807760141093473
Evaluation results (Accuracy): 0.99917
Evaluation results (Precision): 0.18765432098765433
Evaluation results (Recall): 0.4691358024691358

* Note:
  * There are no results for tf-idf as they took long to run, but it passed the pytest and I ran on a small dataset.


## Exact
In exact, we can see that the precision is 100% while recall is very low, this is because only exact matches are taken. For example in Recall, many matches are not exact macthes, such as John and Jon. 

We can see that the accuracy is misleading as the classes are imbalanced, f1 gives us a better understanding. Most classes are predicted to be 0, which is what the tsv had.


## Jaccard

testing different threshhold, we can see that 0.5 is the closest to the optimal threshhold. Resulting in the highest f1 score.

## Levenshtein

Levenshtein captures distance between characters, so it recognize s matches with different minor spellings. Compared to Jaccard, it achieves higher recall at threshold 0.5 but lower precision. 

the results from training and testing are kind of similar, showing that the model is not overfitting. 

All and all, Jaccard showed to be the best implementation, as it surprasses all other methods when the threshhold is 0.5, especially looking at the f1 accuracy. 
