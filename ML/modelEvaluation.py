import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_classification_model(y_true, y_pred, labels=None):
    """
    Calculates and displays common classification metrics and a confusion matrix.

    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels.
        labels (list, optional): List of class labels for confusion matrix. Defaults to None.
    """
    print("--- Model Evaluation Report ---")

    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='binary', pos_label=1) # Assuming positive class is 1
    recall = recall_score(y_true, y_pred, average='binary', pos_label=1)
    f1 = f1_score(y_true, y_pred, average='binary', pos_label=1)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")

    # Display Confusion Matrix
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=labels if labels else ['Negative', 'Positive'],
                yticklabels=labels if labels else ['Negative', 'Positive'])
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

# Example Usage:
# Simulate true labels and predictions for a binary classification problem
y_true_example = np.array()
y_pred_example = np.array()

evaluate_classification_model(y_true_example, y_pred_example, labels=['Non-Fraud', 'Fraud'])

# Example with imbalanced data (e.g., fraud detection)
y_true_imbalanced = np.array() # 9 negatives, 1 positive
y_pred_imbalanced = np.array() # Model predicted 1 fraud, 1 false positive

print("\n--- Evaluation for Imbalanced Data ---")
evaluate_classification_model(y_true_imbalanced, y_pred_imbalanced, labels=['Non-Fraud', 'Fraud'])