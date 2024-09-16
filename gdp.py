"""
GDP data can be found: https://bea.gov/itable/national-gdp-and-personal-income
"""

import pandas as pd

data = pd.read_csv('Data/GDP_data.csv')

# Remove: Change in private inventories, Net exports of goods and services, Addendum:
df = data.drop(columns='Change in private inventories')
df = df.drop(columns='Net exports of goods and services')
df = df.drop(columns='Addendum:')
print(df.columns)
