#03-07-2026
#Scikit library in python
#It's an open source python library and it provides tools for data analysis and predictive modelling.

#Key Features
#1 - Data preprocessing - this involves data splitting, feature scaling, feature selection, feature extraction
#2 - Data splitting - training and testing sets
#3 - feature engineering - this involves selection of important features fromyour data to improve  model performance.
# RESEARCH (4 - Scaling, different scaling, comparison btn them, when to use which.)

#Absolute Maximum Scaling - it is sensitive to outliers and best for clean data.

import pandas as pd
import numpy as np

df = pd.read_csv("Housing.csv")  # fixed: underscore not hyphen

# Keep only numeric columns for scaling
df_numeric = df.select_dtypes(include=np.number)

# Max absolute value per column to use for scaling
max_abs = np.max(np.abs(df_numeric), axis=0)
print("Max absolute: ", max_abs)

# Scale to [-1, 1] range by max-abs scaling. Avoid division by zero.
max_abs_safe = max_abs.replace(0, 1)  # if a column is all 0s
scaled_df = df_numeric / max_abs_safe

print("Scaled head:")
print(scaled_df.head())
print("\nScaled max abs values: ")
print(np.max(np.abs(scaled_df), axis=0))
#2 - model Evalution
#3 pipeline support
# supports integration
# easy to use

#machine supervised learning - classification e. logistic regression, random forest etc and regression eg linear regression, decision trees

