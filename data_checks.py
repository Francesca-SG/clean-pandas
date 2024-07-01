import pandas as pd
from scipy import stats
import numpy as np

def empty_dataframe(df):
    """Checks if the DataFrame is empty and prints the result."""
    if df.empty:
        print("df is empty.")
    else:
        print("df not empty.")

def check_missing_values(df):
    """Prints the number of missing values for each column in the DataFrame."""
    missing_values = df.isnull().sum()
    print(missing_values)

def duplicate_company_name(df):
    """Finds and prints duplicate values in the 'company' column."""
    duplicates = df[df.duplicated('company', keep=False)]
    print(duplicates.sort_values('company'))

def is_empty_column(df):
    """Checks if 'employees' column exists and contains numerical data."""
    if 'employees' in df.columns:
        if pd.api.types.is_numeric_dtype(df['employees']):
            print("'employees' column exists and contains numerical data.")
        else:
            print("'employees' column exists but does not contain numerical data.")
    else:
        print("'employees' column does not exist.")

def unique_ranks(df):
    """Prints the number of unique ranks in the 'rank' column."""
    num_unique_ranks = df['rank'].nunique()
    print(f'There are {num_unique_ranks} unique ranks.')

def show_duplicates(df):
    """Finds and prints duplicate rows based on the 'rank' column."""
    duplicates_mask = df.duplicated(subset='rank', keep=False)
    duplicate_rows = df[duplicates_mask]
    print(duplicate_rows)

def show_outliers(df):
    """Finds and prints outliers in the 'revenue' column using z-scores."""
    z_scores = np.abs(stats.zscore(df['revenue']))
    outliers = df[z_scores > 3]
    print(outliers)