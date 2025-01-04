import pandas as pd
import numpy as np

# Load the dataset
file_path = "raw_medium_dataset.csv"  # Ensure this matches the uploaded file name
data = pd.read_csv(file_path)

# Display the first few rows before cleaning
print("Original Data Sample:")
print(data.head())

# Step 1: Handle Missing Values
# Fill missing numeric values with the median
numeric_columns = data.select_dtypes(include=[np.number]).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

# Fill missing categorical values with the mode
categorical_columns = data.select_dtypes(include=['object']).columns
for col in categorical_columns:
    data[col] = data[col].fillna(data[col].mode()[0])

# Step 2: Remove Duplicates
data = data.drop_duplicates()

# Step 3: Standardize Date Format
if 'purchase_date' in data.columns:
    data['purchase_date'] = pd.to_datetime(data['purchase_date'], errors='coerce')

# Step 4: Normalize Text Columns (strip whitespace and convert to lowercase)
for col in categorical_columns:
    data[col] = data[col].str.strip().str.lower()

# Step 5: Export Cleaned Data
cleaned_file_path = "cleaned_medium_dataset.csv"
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
