import pandas as pd

# Load dataset
df = pd.read_csv("data/flipkart_reviews.csv")

# Show first 5 rows
print("🔹 First 5 rows:")
print(df.head())

# Show column names
print("\n🔹 Columns:")
print(df.columns)

# Show basic info
print("\n🔹 Info:")
print(df.info())

# Check missing values
print("\n🔹 Missing values:")
print(df.isnull().sum())
