# Messy CSV to Clean Report

A data cleaning and analysis project using Pandas on a synthetic, deliberately messy food delivery orders dataset (292 rows).

## The mess

- 20 inconsistent spellings/casings of 5 real categories (e.g. "ITALIAN", "italian", "Itallian")
- Inconsistent city name casing and whitespace
- 4 different date formats mixed in the same column
- Currency symbols mixed into a numeric column
- Missing values across amount, delivery time, and customer rating
- 12 duplicate rows
- A handful of unrealistic outlier values (negative and 200+ minute delivery times)

## Cleaning steps

1. Diagnosed missing values and duplicates before making any changes
2. Standardized category names using a manual mapping dictionary
3. Fixed city name whitespace/casing using str.strip() and str.title()
4. Parsed mixed date formats into a consistent datetime column using pd.to_datetime(format="mixed")
5. Stripped currency symbols and converted amount to numeric
6. Removed duplicate rows
7. Filled missing numeric values with each column's median
8. Identified and corrected outlier delivery times using describe() and conditional .loc[]
9. Exported the cleaned dataset to cleaned_orders.csv

## Analysis

Answered 10 business questions using groupby, value_counts, pivot_table, and correlation, including:
- Average order amount by category and by city+category combined
- Which city generates the most orders and revenue
- Which restaurant has the fastest delivery and highest rating
- Whether delivery time and customer rating are correlated (they aren't - correlation of 0.08)

## Usage

Run the script:
python clean.py

This prints the diagnostic steps, cleaning confirmations, and all 10 analysis answers, and saves cleaned_orders.csv.

## What I learned
- Diagnosing data quality issues systematically before fixing anything (isnull().sum(), duplicated().sum(), unique(), describe())
- The difference between problems needing a manual mapping (typos) vs. built-in string methods (whitespace/casing)
- Why to_datetime() needs format="mixed" for inconsistent date formats, and why it doesn't auto-detect this by default
- How Pandas handles NaN gracefully during string and numeric transformations, rather than crashing
- Choosing median over mean for filling missing values, due to outlier sensitivity
- The difference between .max()/.min() (the value) and .idxmax()/.idxmin() (which group has that value) - and how picking the wrong aggregation function fails silently rather than crashing
- groupby for single-dimension aggregation vs. pivot_table for two-dimension aggregation
- Correlation as a way to test a hypothesis against real data, including when the honest answer is "no relationship found"