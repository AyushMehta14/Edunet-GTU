import pandas as pd

# Import Dataset
df = pd.read_csv("global-data-on-sustainable-energy (1).csv")

# ==========================
# BASIC INFORMATION
# ==========================

print("First 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nShape of Dataset")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ==========================
# NULL VALUES
# ==========================

print("\nNull Values in Each Column")
print(df.isnull().sum())

# Fill numerical columns with mean
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill object columns with mode
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nNull Values After Cleaning")
print(df.isnull().sum())

# ==========================
# CORRELATION
# ==========================

print("\nCorrelation Matrix")
print(df.corr(numeric_only=True))

# ==========================
# GENERALISATIONS AND ANALYSIS
# ==========================

# The dataset contains sustainability and energy information of different countries.

# Access to Electricity and GDP per Capita are generally positively related.

# Countries with high renewable energy production usually depend less on fossil fuels.

# CO2 emissions generally increase with energy consumption.

# Population growth can increase electricity demand.

# Renewable energy percentage and carbon emissions may have a negative relationship.

# Countries with better access to clean fuels generally have higher development levels.

# The correlation matrix helps identify which features are strongly related.

# Missing values were handled by:
# 1. Mean for numerical columns.
# 2. Mode for text columns.

# ==========================
# EXTRA ANALYSIS
# ==========================

print("\nNumber of Missing Values after Cleaning:")
print(df.isnull().sum().sum())

print("\nNumber of Rows and Columns:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# ==========================
# SUMMARY
# ==========================

"""
SUMMARY

1. Imported the sustainability dataset using pandas.
2. Displayed first and last rows of the dataset.
3. Displayed shape, columns, and statistical information.
4. Checked for null values.
5. Replaced numerical null values with mean.
6. Replaced text null values with mode.
7. Generated correlation matrix to study relationships.
8. Added observations and generalisations about sustainability indicators.
9. Prepared the dataset for further analysis and visualization.
"""