import pandas as pd

# Checks that the dataframe for data
def empty_dataframe(df):
    if df.empty:
        print("df is empty.")
    else:
        print("df not empty.")

# Function that checks for missing values, gives a summary for each column
def check_missing_values(df):
    missing_values = df.isnull().sum()
    print(missing_values)


# Looks for duplicate values in a specific column and doesn't modify them
def duplicate_company_name(df):
    duplicates = df[df.duplicated('company_name', keep=False)]
    print(duplicates.sort_values('company_name'))


# Checks if the 'current_worker_count' column exists and contains numerical data
def is_empty_column(df):
    if 'current_worker_count' in df.columns:
        if pd.api.types.is_numeric_dtype(df['current_worker_count']):
            print("'current_worker_count' column exists and contains numerical data.")
        else:
            print("'current_worker_count' column exists but does not contain numerical data.")
    else:
        print("'current_worker_count' column does not exist.")