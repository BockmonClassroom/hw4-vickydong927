'''
Name: Weiqi Dong
Date: 2/15/2025
'''
# Step 1: Import Libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Step 2: Load the Dataset
# Load the Iris dataset
df = pd.read_csv('data/Iris.csv')

# Step 3: Normalize the Data
# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Normalize the numeric columns (excluding the 'Species' column)
normalized_data = scaler.fit_transform(df.iloc[:, :-1])

# Create a new DataFrame with the normalized data
normalized_df = pd.DataFrame(normalized_data, columns=df.columns[:-1])

# Add the 'Species' column back
normalized_df['Species'] = df['Species']

# Save the normalized data to a new CSV file
normalized_df.to_csv('data/Iris_normalized.csv', index=False)

# Step 4: Standardize the Data
# Initialize the StandardScaler
scaler = StandardScaler()

# Standardize the numeric columns (excluding the 'Species' column)
standardized_data = scaler.fit_transform(df.iloc[:, :-1])

# Create a new DataFrame with the standardized data
standardized_df = pd.DataFrame(standardized_data, columns=df.columns[:-1])

# Add the 'Species' column back
standardized_df['Species'] = df['Species']

# Save the standardized data to a new CSV file
standardized_df.to_csv('data/Iris_standardized.csv', index=False)