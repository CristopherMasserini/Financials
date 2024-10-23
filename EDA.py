"""
File for exploring the data for trends to be used in modeling
"""

import pandas as pd


def run_correlations(df):
    # Ignore Year, Quarter
    # Use Gross domestic product vs everything else
    print(df['Gross domestic product'].corr(df['Personal consumption expenditures']))


if __name__ == '__main__':
    data = pd.read_csv('Data/GDP_data_cleaned.csv')
    run_correlations(data)
