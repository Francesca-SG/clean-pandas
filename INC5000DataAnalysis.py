#imports libraries
import os
import pandas as pd 
from scipy import stats
import numpy as np
#import modules
import data_checks


# Gets the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Builds the path to the file
file_path = os.path.join(script_dir, 'INC5000_Companies_2019.csv')

# Reads the CSV file
# Data Frame (df) is a 2 dimensional data structure, like an array or table, with columns and rows
df = pd.read_csv(file_path)


# Renames columns in table and assigns it back to the dataframe, saving the changes
df = df.rename(columns={'workers':'current_worker_count', 'previous_workers':'previous_worker_count', 'name':'company_name'})

# Fills null with a value in this case the mean 
df['current_worker_count']= df['current_worker_count'].fillna(df['current_worker_count'].mean())
df['metro'] = df['metro'].fillna('Not Applicable') 


# Returns boolean value for each row
# Print(df.duplicated())

data_checks.check_missing_values(df)

# Function looks for duplicate values in a specific 
data_checks.duplicate_company_name(df)

# Uses title case to make all string values in the city column first letter caps, rest lower case
df['city'] = df['city'].str.title()

# Prints if dataframe is empty or not 
data_checks.empty_dataframe(df)

# Check if the 'current_worker_count' column exists and contains numerical data
data_checks.is_empty_column(df)

def convert_revenue(value):
    if 'Million' in value.lower():
        # Removes 'Million', converts to float and mulitiplies by 1e6
        value = value.replace('Million','').strip()
        return float(value) * 1e6

# Apply the function to the 'revenue' column   
df['revenue'] = df['revenue'].apply(convert_revenue)

##Bug here, revenue column returning none I think I know how to fix.

#z_scores = np.abs(stats.zscore(df['current_worker_count']))
# This will show the outliers
#outliers = df[(z_scores > 3)]

# Prints the first 5 rows of the table, df.tail prints the last 5
print(df.head())
print(df.tail())

# Prints the column names, number of not nulls in each and the data types.
#print(df.info())
#print(df.columns)


