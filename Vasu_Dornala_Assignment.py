# Task 1 : Load the dataset into Dataframe called df. Set order_id as the row index at load time. Display the first 5 rows and the last 5 rows.
print("\n# Task 1 : Load the dataset into Dataframe called df. Set order_id as the row index at load time. Display the first 5 rows and the last 5 rows.")

import numpy as np
import pandas as pd

# Download CSV file and load the dataset into Dataframe df
url = "https://drive.google.com/uc?export=download&id=1Mlu9r3afSGz5_02Y3wDJoQLpXszQXaIU"
print("\n1a. The csv dataset is loaded into pandas data frame")

# Read the CSV, setting 'order_id' as the row index at load time
df = pd.read_csv(url, index_col='order_id')
print("\n and The 'order_id' is set as the row index")

# Display the first 5 rows

print("\n1b. First 5 rows of the DataFrame:")
print("\n")
print(df.head())

# Display the last 5 rows
print("\n1c.  Last 5 rows of the DataFrame:")
print("\n")
print(df.tail())
print("\n")

# Task 2 : Run a structural inspection of df. From the output, answer the following in a markdown cell
print("\nTask 2 : Run a structural inspection of df. From the output, answer the following in a markdown cell")
print("\n")

# to find the full structural summary of dataset
df.info

# to find the total number of rows and coumns, use print(df.shape)
print(f"\n2a. how many rows and columns does the data set have?")
print(f"\nTotal Rows: {df.shape[0]}")
print(f"\nTotal Columns: {df.shape[1]}")
print("\n")

# find how many columns have missing values and how many nulls does each have
print(f"\n2b. Which columns have missing values and how many nulls does each have?")
print(f"\nFollowing are the columns with null values")
print("\n")
print(df.isnull().sum())
print("\n")

# Task 3 : Run a statistical summary of the numeric columns. From the output, answer the following in a markdown cell:
print("\nTask 3 : Run a statistical summary of the numeric columns. From the output, answer the following in a markdown cell:")
print("\n")
# to find statistical summary of the dataset, use df.describe()
summary = df.describe()
print(summary)
print("\n")

# what is the median unit_price
print(f"\n3a. What is the median unit_price?")
print(f"\nMedian Unit Price: {summary['unit_price']['50%']}")
print("\n")

# Does unit_price appear to be skewed? Explain using values from the output.
print(f"\n3b. Does unit_price appear to be skewed? Explain using values from the output.")

mean_val = df['unit_price'].mean()
median_val = df['unit_price'].median()

print(f"\nMean: {mean_val:.2f}")
print(f"\nMedian: {median_val:.2f}")

if mean_val > median_val:
    print("\nThe Mean is greater than the Median and hence the 'unit_price' is skewed (Right Skew).")
else:
    print("\nThe Mean is not greater than the Median.")
    print("\nThe 'unit_price' is not skewed (Left Skew).")
print("\n")








