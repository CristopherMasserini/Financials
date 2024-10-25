"""
File for exploring the data for trends to be used in modeling
"""

import pandas as pd


def run_correlations(df):
    # Ignore Year, Quarter
    # Use Gross domestic product vs everything else
    print(df['Gross domestic product'].corr(df['Personal consumption expenditures']))


def trailing(df):
    # Trailing average of previous 4 quarters
    col = 'Personal consumption expenditures'
    col_data = df.loc[:, col]
    dataNew = {'Year Quarter': df.loc[4:, 'Year Quarter'],
               'GDP': df.loc[4:, 'Gross domestic product'],
               col: []}

    init_trail_range = [0, 1, 2, 3]
    for i in range(0, len(dataNew['Year Quarter'])):
        sum = 0
        for j in init_trail_range:
            sum += col_data[j]
        dataNew[col].append(sum / 4)

        init_trail_range = [x + 1 for x in init_trail_range]

    return dataNew


if __name__ == '__main__':
    data = pd.read_csv('Data/GDP_data_cleaned.csv')
    # run_correlations(data)
    trailing(data)
