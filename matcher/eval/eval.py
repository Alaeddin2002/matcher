from sklearn import metrics

def evaluate(results, metric_name):
    
    # extract labels from list of dicts
    true_labels = [row["true_label"] for row in results]
    predicted_labels = [row["predicted_label"] for row in results]
    
    if metric_name == 'accuracy':
        return metrics.accuracy_score(true_labels, predicted_labels)
    
    elif metric_name == 'precision':
        return metrics.precision_score(true_labels, predicted_labels, zero_division=0)
    
    elif metric_name == 'recall':
        return metrics.recall_score(true_labels, predicted_labels, zero_division=0)
    
    elif metric_name == 'f1':
        return metrics.f1_score(true_labels, predicted_labels, zero_division=0)
    
    else:
        raise ValueError(f"Unknown metric: {metric_name}")