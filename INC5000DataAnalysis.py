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
df = df.rename(columns={'workers':'current_worker_count', 'previous_workers':'previous_worker_count', 'name':'company_name'})

# Fills null with a value in this case the mean 
df['current_worker_count']= df['current_worker_count'].fillna(df['current_worker_count'].mean())
df['metro'] = df['metro'].fillna('Not Applicable') 

# Converts column data type to integers
df['current_worker_count']= df['current_worker_count'].astype(int)

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


# This codw would have been fine if it were only used to replace one value
#def convert_revenue(value):
#df['revenue'] = df['revenue'].astype(str).replace(['Million', 'Billion'], '', regex=True)
#df['revenue'] = df['revenue'].astype(str).str.replace('Billion', '')
#df['revenue'] = df['revenue'].astype(float)
#df['revenue'] = df['revenue'] * 1e6 

# Replaces the values and converts to float, multiplies for correct value
def convert_revenue(value):
    value = value.replace(',', '')
    if 'Billion' in value:
        value = value.replace('Billion', '').strip()
        return float(value) * 1e9
    elif 'Million' in value:
        value = value.replace('Million', '').strip()
        return float(value) * 1e6
    else:
        return float(value)

df['revenue'] = df['revenue'].apply(convert_revenue)

#dt = df.dtypes
#print(dt)


#z_scores = np.abs(stats.zscore(df['current_worker_count']))
# This will show the outliers
#outliers = df[(z_scores > 3)]

# Prints the first 5 rows of the table, df.tail prints the last 5
print(df.head())
print(df.tail())

# Prints the column names, number of not nulls in each and the data types.
#print(df.info())
#print(df.columns)


