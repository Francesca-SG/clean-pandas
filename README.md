# Data Analysis Project


## Introduction
This project involes analysing a dataset of INC 5000 companies from 2019. The goal of this project is to gain insights into the characteristics of these companies and understand the factors that influence their revenue and growth. The dataset was made available 

## Project Description
This project involves a comprehensive analysis of a dataset somprising of INC 5000 companies in 2019. Thee datset provides a unique opportunity to delve into the characteristics, growth patterns, and revenue details of high-performing companies across various industries.

The primary objective of this project is to uncover meaningful insights about these companies using data analysis techniques. These insights include, understanding the correlation between revenue and industry, the distribution of these companies by state and size of workforce compared to percentage growth.

Usually the question is defined before the data is collected. However, for the purposes of this project the data was collected before and then the questions defined.

The project is divided into five stages:
- Collecting the data 
- Defining the question 
- Cleaning the data
- Analysing the data
- Visualise and share the findings

As part of this project, I am continuously working to enhance my skills and understanding of Python, Pandas and visualisation tools like Power BI. Additionally, I plan to move the data to SQL to practice data manipulation and querying.


## Questions Explored
In this project, my aim is to answer the following questions:
1. Which industry has the highest and lowest average revenue?
2. How does the growth percentage vary across different industries?
3. Is there any correlation between a companies founding year and  its percentage growth?
4. Has the distribution of industries changed for companies founded  in more recent years compared to those founded earlier?
5. Which states have the highest average company growth percentages?
6. Do companies with higher percentage growth tend to have more employees compared to those with lower growth?


## Results and Insights
# Initial Insights
- These are some initial insights gleaned from simply looking at the data:
    - The data shows a variety of industries, company sizes, and locations.
    - The'Consumer Products & Services' industry is well represented. 
    - Most companies appear to be founded in recent years. 
    - Columns like 'url' and 'profile' may not be relevant for data analysis.
    - There are missing values and data type inconsistencies that need to be addressed.
    - Some column names need to be clearer.

# Insights Gained During Data Cleaning Process
**Dataset Overview**: The dataset is intended to rank the top 5000 companies in the US by revenue growth. However, the data contains more than 5000 unique companies.
**Rank Duplication**: In rare cases, some companies share the same rank. This indicates the ranking system may allow for ties.
**Revenue Outliers**: There where a few examples of high-revenue outliers, this is expected in a dataset of high performing companies.
**Rank and Revenue Discrepancy**: Some high-revenue companies have lower ranks, suggesting the ranking system is based on growth percentage rather than revenue.
**Data Errors**: Some of the minimum values in specific columns are clearly erroneous e.g. current employee count at 0.


# Data Cleaning 
- Utilised Python, Pandas to clean the data. The steps included:
    - Handling missing values
    - Renaming columns for clarity
    - Checking for duplicate entries
    - Modifying data types for consistency
    - Removing irrelevant columns 
    - Removing rows with inaccurate data
    - Checking for outliers 


## Skills Demonstrated
- Data cleaning
    - Handling missing values
    - Renaming columns
    - Checking for outliers
    - Clean and organised code


## Technology Used
- Python
    - Pandas 
    - NumPy
    - SciPY


## Viewing the Project
You can view the Python code for this project in the `INC5000DataAnalysis.py`, and `data_checks.py` file.The first file contains data cleaning code, the second has functions for checking the data. The `INC5000_Companies_2019.csv` file contains the original dataset I worked with.

