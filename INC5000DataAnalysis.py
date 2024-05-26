#imports libraries
import pandas as pd 
import os
from scipy import stats
import numpy as np

#Data Frame (df) is a 2 dimensional data structure, like an array or table, with columns and rows
df = pd.read_csv('C:\\Users\\Francesca\\Documents\\Coding Projects\\DataAnalysisProject\\INC5000_Companies_2019.csv')

#renames columns in table
df.rename(columns={'workers':'current_worker_count', 'previous_workers':'previous_worker_count', 'name':'company_name'}, inplace=True)
#df = df.rename(columns={'workers':'current_worker_count', 'previous_workers':'previous_worker_count', 'name':'company_name'})

#fills null with a value in this case the mean 
df['current_worker_count'].fillna(df['current_worker_count'].mean())
df['metro'].fillna('Not Applicable') 

#checks for missing values, gives a summary for each column
missing_values = df.isnull().sum()

#prints duplicates with True, prints False if none
#print(df.duplicated())

#looks for duplicate values in a specific column and doesn't modify them
duplicates = df[df.duplicated('company_name', keep=False)]
print(duplicates.sort_values('company_name'))

#uses title case to make all string values in the city column first letter caps, rest lower case
df['city'] = df['city'].str.title()

#prints if dataframe is empty or not
if df.empty:
    print("The DataFrame is empty.")
else:
    print("The DataFrame is not empty.")

# Check if the 'current_worker_count' column exists and contains numerical data
if 'current_worker_count' in df.columns:
    if pd.api.types.is_numeric_dtype(df['current_worker_count']):
        print("The 'current_worker_count' column exists and contains numerical data.")
    else:
        print("The 'current_worker_count' column exists but does not contain numerical data.")
else:
    print("The 'current_worker_count' column does not exist.")


z_scores = np.abs(stats.zscore(df['current_worker_count']))
# This will show the outliers
outliers = df[(z_scores > 3)]

#prints the first 5 rows of the table, df.tail prints the last 5
print(df.tail())
#prints the column names, number of not nulls in each and the data types.
print(df.info())
print(df.columns)
print(outliers)

