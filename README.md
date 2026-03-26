# 📊 Flipkart Customer Sentiment & Product Analysis

## 🚀 Project Overview

This project analyzes Flipkart customer reviews to understand how product pricing, ratings, and customer feedback influence overall sentiment.

It demonstrates a complete end-to-end data analysis workflow by integrating Python, SQL, and Excel into an automated pipeline.

---

## 🧠 Problem Statement

How do product price and customer ratings impact customer sentiment and product perception on Flipkart?

---

## ⚙️ Workflow

1. **Data Loading**

   * Imported raw dataset using Python

2. **Data Cleaning & Preprocessing**

   * Handled missing values
   * Converted price and rating to numeric format
   * Cleaned text fields

3. **Feature Engineering**

   * Created new features:

     * Price Range (Low / Medium / High)
     * Rating Category (Poor / Average / Good)
     * Review Length

4. **SQL Integration**

   * Stored cleaned data in SQLite database
   * Performed analysis using SQL queries

5. **Data Analysis**

   * Sentiment distribution
   * Price range distribution
   * Rating category insights

6. **Excel Reporting**

   * Automatically generated Excel report
   * Multiple sheets for different insights

---

## 🛠️ Tech Stack

* Python (Pandas)
* SQL (SQLite)
* Excel (Reporting & Visualization)
* VS Code

---

## 📊 Key Insights

* Majority of customer reviews are positive
* Medium-priced products dominate the dataset
* Higher ratings are strongly associated with positive sentiment
* Low-rated products show higher negative sentiment

---

## 📁 Project Structure

flipkart-customer-analysis/
│
├── pipeline.py → Full automation script
├── Raw_Dataset.csv → Dataset
├── flipkart_report.xlsx → Final Excel report
├── flipkart.db → SQLite database

---

## 🚀 How to Run

1. Open `pipeline.py`
2. Run the script
3. The Excel report will be generated automatically

---

## 📂 Dataset Source

This project uses a publicly available Flipkart customer reviews dataset from Kaggle:

👉 https://www.kaggle.com/datasets/niraliivaghani/flipkart-product-customer-reviews-dataset

---

## 🎯 Outcome

Built a complete end-to-end data analysis pipeline combining:

* Data cleaning (Python)
* Data querying (SQL)
* Data reporting (Excel)

This project demonstrates real-world data analyst workflow and automation.

---

## 👩‍💻 Author

Robina Shakwa
