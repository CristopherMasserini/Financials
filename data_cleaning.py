"""
GDP data can be found: https://bea.gov/itable/national-gdp-and-personal-income
"""

import pandas as pd


def read_data():
    data = pd.read_csv('Data/GDP_data.csv')

    return data


def clean_data(df):
    # Remove: Change in private inventories, Net exports of goods and services, Addendum:
    # These are blank throughout the sheet
    df = df.drop(columns='Change in private inventories')
    df = df.drop(columns='Net exports of goods and services')
    df = df.drop(columns='Addendum:')

    # Create a column combining year and quarter
    df['Year Quarter'] = df['Year'].astype(str) + df['Quarter'].astype(str)

    df = df.drop(columns='Year')
    df = df.drop(columns='Quarter')
    return df


def save_dataframe(df):
    # Plotting done in Tableau at:
    # https://public.tableau.com/app/profile/cristopher.masserini/viz/Financials_17284199840920/Sheet1
    df.to_csv('Data/GDP_data_cleaned.csv', index=False)


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
    data = read_data()
    data = clean_data(data)
    save_dataframe(data)
