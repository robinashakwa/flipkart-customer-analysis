import pandas as pd
import sqlite3
import subprocess
import sys

print("🚀 Starting Flipkart Data Pipeline...\n")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(
    "C:/Users/hp/Downloads/Raw_Dataset.csv",
    encoding="latin1",
    on_bad_lines='skip'
)

print("✅ Dataset loaded successfully!\n")

# =========================
# DATA CLEANING
# =========================

# Fix column names
df.columns = df.columns.str.lower()

# Convert to numeric
df['product_price'] = pd.to_numeric(df['product_price'], errors='coerce')
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

# Handle missing values
df['review'] = df['review'].fillna("No Review")
df['summary'] = df['summary'].fillna("No Summary")

# Clean product name
df['product_name'] = df['product_name'].str.replace(r'[^\x00-\x7F]+', '', regex=True)

# =========================
# FEATURE ENGINEERING
# =========================

# Price range
df['price_range'] = pd.cut(
    df['product_price'],
    bins=[0, 1000, 5000, 100000],
    labels=['Low', 'Medium', 'High']
)

# Rating category
df['rating_category'] = pd.cut(
    df['rate'],
    bins=[0, 2, 4, 5],
    labels=['Poor', 'Average', 'Good']
)

# Review length
df['review_length'] = df['review'].apply(len)

print("✅ Data cleaning completed!\n")

# =========================
# SAVE TO SQL
# =========================

print("🚀 Moving data to SQL...\n")

conn = sqlite3.connect("flipkart.db")

df.to_sql("flipkart_data", conn, if_exists="replace", index=False)

print("✅ Data successfully stored in SQL database!\n")

# =========================
# SQL QUERIES
# =========================

print("📊 Running SQL Queries...\n")

# Sentiment Analysis
query1 = """
SELECT sentiment, COUNT(*) as total_reviews
FROM flipkart_data
GROUP BY sentiment
"""
result1 = pd.read_sql_query(query1, conn)

print("🔹 Sentiment Distribution:")
print(result1)

# Price Analysis
query2 = """
SELECT price_range, COUNT(*) as total
FROM flipkart_data
GROUP BY price_range
"""
result2 = pd.read_sql_query(query2, conn)

print("\n🔹 Price Range Distribution:")
print(result2)

# Rating Analysis
query3 = """
SELECT rating_category, COUNT(*) as total
FROM flipkart_data
GROUP BY rating_category
"""
result3 = pd.read_sql_query(query3, conn)

print("\n🔹 Rating Category Distribution:")
print(result3)

# =========================
# EXPORT TO EXCEL
# =========================

print("\n📊 Exporting results to Excel...\n")

# Auto-install openpyxl if needed
try:
    import openpyxl
except ModuleNotFoundError:
    print("📦 Installing openpyxl...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])

with pd.ExcelWriter("C:/Users/hp/Downloads/flipkart_report.xlsx", engine="openpyxl") as writer:
    
    result1.to_excel(writer, sheet_name="Sentiment Analysis", index=False)
    result2.to_excel(writer, sheet_name="Price Analysis", index=False)
    result3.to_excel(writer, sheet_name="Rating Analysis", index=False)

print("✅ Excel file created: flipkart_report.xlsx")

# Close connection
conn.close()

print("\n🎉 FULL PIPELINE COMPLETED SUCCESSFULLY!")
