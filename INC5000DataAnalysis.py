#imports libraries
import pandas as pd 
import os

#Data Frame (df) is a 2 dimensional data structure, like an array or table, with columns and rows
df = pd.read_csv('C:\\Users\\Francesca\\Documents\\Coding Projects\\DataAnalysisProject\\INC5000_Companies_2019.csv')

#renames columns in table
df = df.rename(columns={'workers':'current_worker_count', 'previous_workers':'previous_worker_count',})

#prints the first 5 rows of the table, df.tail prints the last 5
print(df.head())
print(df.info())

