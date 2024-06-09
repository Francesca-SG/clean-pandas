#imports libraries
import os
import pandas as pd 
from scipy import stats
import numpy as np
#import modules
import data_checks


# Function gets directory of current script, builds the path to the file, and read files
def read_data(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # Data Frame (df) is a 2D data structure, like an array or table
    df = pd.read_csv(file_path)
    return df

df = read_data('INC5000_Companies_2019.csv')

# Renames columns in table and assigns it back to the dataframe, saving the changes
df = df.rename(columns={'workers':'employees', 'previous_workers':'former_employees', 'name':'company'})

# Fills null with a value in this case the mean 
df['employees']= df['employees'].fillna(df['employees'].mean())
df['metro'] = df['metro'].fillna('Not Applicable') 

# Converts column data type to integers
df['employees']= df['employees'].astype(int)

# Returns boolean value for each row
# Print(df.duplicated())

# removes columns, axis 1=column and 0=row
df = df.drop('url', axis=1)
df = df.drop('profile', axis=1)


data_checks.check_missing_values(df)

# Function looks for duplicate values in a specific 
data_checks.duplicate_company_name(df)


# Uses title case to make all string values in the city column first letter caps, rest lower case
df['city'] = df['city'].str.title()

# Prints if dataframe is empty or not 
data_checks.empty_dataframe(df)

# Check if the 'employees' column exists and contains numerical data
data_checks.is_empty_column(df)


# Replaces the values and converts to float, to handle the multiplication, then converts to int
def convert_revenue(value):
    value = value.replace(',', '')
    if 'Billion' in value:
        value = value.replace('Billion', '').strip()
        return int(float(value) * 1e9)
    elif 'Million' in value:
        value = value.replace('Million', '').strip()
        return int(float(value) * 1e6)
    else:
        return int(float(value))

df['revenue'] = df['revenue'].apply(convert_revenue)

#dt = df.dtypes
#print(dt)

# Rounds the values in the values in column to a whole number
df['growth_%'] =  df['growth_%'].round(0)
df['growth_%'] =  df['growth_%'].astype(int)

# This splits the string at the comma and only keeps the first part
df['metro'] = df['metro'].str.split(',').str[0]


# Checks for unique ranks and prints each row
data_checks.unique_ranks(df)
data_checks.show_duplicates(df)

# Removes specific row from dataframe, based on the condition 'rank' is 4997
df = df.drop(df[(df['rank'] == 4997)].index)


print('this is the standard deviation')
data_checks.show_outliers(df)

# Prints the first 5 rows of the table, df.tail prints the last 5
#print(df.head())
#print(df.tail())


# Returns the data from a specified row 
print(df.iloc[7])

# Gives a summary of the main characteristics of the dataset
print(df.describe())
# Prints the column names, number of not nulls in each and the data types.
#print(df.info())
#print(df.columns)


