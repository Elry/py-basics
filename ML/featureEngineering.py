import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

def perform_feature_engineering(df):
    """
    Performs feature engineering:
    1. Creates interaction features.
    2. Creates polynomial features.
    3. Applies one-hot encoding to categorical variables.
    """
    print("Original DataFrame head:\n", df.head())

    # Identify numerical and categorical columns
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = df.select_dtypes(include='object').columns.tolist()

    # Step 1: Create Interaction Features (simple multiplication example)
    # Assuming 'numerical_col_1' and 'numerical_col_2' are in numerical_cols
    if 'numerical_col_1' in numerical_cols and 'numerical_col_2' in numerical_cols:
        df['interaction_feature'] = df['numerical_col_1'] * df['numerical_col_2']
        print("\nCreated 'interaction_feature'.")
        # Add the new feature to numerical_cols for subsequent transformations if needed
        numerical_cols.append('interaction_feature')
    else:
        print("\nSkipping interaction feature: 'numerical_col_1' or 'numerical_col_2' not found.")

    # Step 2: Create Polynomial Features
    # Use a ColumnTransformer to apply PolynomialFeatures only to numerical columns
    # Exclude the target variable if it's in numerical_cols
    features_for_poly = [col for col in numerical_cols if col!= 'target_variable'] # Assuming 'target_variable' is not to be transformed
    
    if features_for_poly:
        poly_transformer = PolynomialFeatures(degree=2, include_bias=False)
        poly_features = poly_transformer.fit_transform(df[features_for_poly])
        poly_feature_names = poly_transformer.get_feature_names_out(features_for_poly)
        
        # Create a DataFrame for polynomial features and concatenate
        poly_df = pd.DataFrame(poly_features, columns=poly_feature_names, index=df.index)
        df = pd.concat([df.drop(columns=features_for_poly), poly_df], axis=1)
        print(f"Created polynomial features (degree 2) for {features_for_poly}.")
    else:
        print("\nNo numerical features found for polynomial transformation.")

    # Step 3: Apply One-Hot Encoding to categorical variables
    if categorical_cols:
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
            ],
            remainder='passthrough' # Keep other columns (numerical, new poly features)
        )
        
        # Fit and transform the data
        # Need to handle column names after transformation
        transformed_data = preprocessor.fit_transform(df)
        
        # Get feature names after one-hot encoding
        ohe_feature_names = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_cols)
        remaining_features = [col for col in df.columns if col not in categorical_cols]
        
        # Reconstruct DataFrame with new column names
        df_transformed = pd.DataFrame(transformed_data, columns=list(ohe_feature_names) + list(remaining_features), index=df.index)
        print(f"Applied One-Hot Encoding to {categorical_cols}.")
        df = df_transformed
    else:
        print("\nNo categorical columns found for one-hot encoding.")

    print("\nEngineered DataFrame head:\n", df.head())
    print("\nEngineered DataFrame columns:\n", df.columns.tolist())
    return df

# Create a sample DataFrame
data = {
    'numerical_col_1': [4, 2, 5, 1, 3],
    'numerical_col_2': [6, 7, 8, 9, 10],
    'categorical_col_A': [],
    'categorical_col_B': [],
    'target_variable':  # Example target, not transformed
}
df_raw = pd.DataFrame(data)

df_engineered = perform_feature_engineering(df_raw.copy())