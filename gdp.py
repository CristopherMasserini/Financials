"""
GDP data can be found: https://bea.gov/itable/national-gdp-and-personal-income
"""

import pandas as pd

data = pd.read_csv('Data/GDP_data.csv')
print(data.columns)
print(data.head())

# Remove: Change in private inventories, Net exports of goods and services, Addendum
