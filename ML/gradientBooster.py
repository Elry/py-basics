import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import make_classification

def train_and_evaluate_gradient_boosting(X, y):
    """
    Trains and evaluates a Gradient Boosting Classifier.
    """
    print("--- Gradient Boosting Classifier ---")

    # 1. Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training data shape: {X_train.shape}, Test data shape: {X_test.shape}")

    # 2. Define the Gradient Boosting Classifier model
    # Key parameters:
    # n_estimators: Number of boosting stages (trees)
    # learning_rate: Shrinks the contribution of each tree
    # max_depth: Controls the depth of individual trees (weak learners)
    # subsample: Fraction of samples to be used for fitting the individual base learners (Stochastic Gradient Boosting)
    # random_state: For reproducibility
    model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, subsample=0.8, random_state=42)
    print("\nModel initialized with parameters:")
    print(model.get_params())

    # 3. Train the model
    print("\nTraining model...")
    model.fit(X_train, y_train)
    print("Model training complete.")

    # 4. Make predictions on the test set
    y_pred = model.predict(X_test)

    # 5. Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nTest Accuracy: {accuracy:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # Optional: Cross-validation for more robust evaluation
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f"\nCross-validation Accuracy (5-fold): {np.mean(cv_scores):.4f} (+/- {np.std(cv_scores):.4f})")

    return model

# Example Usage:
X_example, y_example = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5, random_state=42)
gb_model = train_and_evaluate_gradient_boosting(X_example, y_example)