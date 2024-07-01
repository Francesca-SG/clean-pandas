import os
import pandas as pd
import data_checks

def read_data(file_name):
    """
    Reads data from a CSV file into a DataFrame.
    
    Parameters:
    file_name (str): The name of the CSV file to read.

    Returns:
    pd.DataFrame: The DataFrame containing the data from the CSV file.
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, file_name)
    df = pd.read_csv(file_path)
    return df

df = read_data('INC5000_Companies_2019.csv')

# Renaming columns for clarity
df = df.rename(columns={
    'workers': 'employees', 
    'previous_workers': 'former_employees', 
    'name': 'company'
})

# Filling missing values in specific columns
df['employees'] = df['employees'].fillna(df['employees'].mean())
df['metro'] = df['metro'].fillna('Not Applicable')

# Converting 'employees' column to integers
df['employees'] = df['employees'].astype(int)

# Removing unnecessary columns
df = df.drop(['url', 'profile'], axis=1)

# Check for missing values
data_checks.check_missing_values(df)

# Look for duplicate company names
data_checks.duplicate_company_name(df)

# Converting 'city' column to title case
df['city'] = df['city'].str.title()

# Check if the DataFrame is empty
data_checks.empty_dataframe(df)

# Check if 'employees' column exists and contains numerical data
data_checks.is_empty_column(df)

def convert_revenue(value):
    """
    Converts revenue string to an integer value.
    
    Parameters:
    value (str): The revenue value as a string.

    Returns:
    int: The revenue value as an integer.
    """
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

# Rounding the values in 'growth_%' column and converting to integers
df['growth_%'] = df['growth_%'].round(0).astype(int)

# Splitting the 'metro' column at the comma and keeping the first part
df['metro'] = df['metro'].str.split(',').str[0]

# Check for unique ranks and print each row
data_checks.unique_ranks(df)
data_checks.show_duplicates(df)

# Removing a specific row from DataFrame based on a condition
df = df.drop(df[df['rank'] == 4997].index)

print('This is the standard deviation')
data_checks.show_outliers(df)

# Printing the data from a specified row
#print(df.iloc[7])

# Summarizing the main characteristics of the dataset
#print(df.describe())

# Optional: Uncomment to export the cleaned DataFrame to a CSV file
# df.to_csv('cleaned_data.csv', index=False)

