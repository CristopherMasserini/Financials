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


def trailing(df, col, quarters=4):
    # Trailing average of previous 4 quarters
    col_name = f'{col}_average{quarters}quarters'
    col_data = df.loc[:, col]
    dataNew = {'Year Quarter': df.loc[quarters:, 'Year Quarter'],
               'GDP': df.loc[quarters:, 'Gross domestic product'],
               col_name: []}

    init_trail_range = list(range(0, quarters))
    for i in range(0, len(dataNew['Year Quarter'])):
        sum = 0
        for j in init_trail_range:
            sum += col_data[j]
        dataNew[col_name].append(sum / 4)

        init_trail_range = [x + 1 for x in init_trail_range]

    pd.DataFrame(dataNew).to_csv(f'Data/{col}_trailing{quarters}quarters.csv', index=False)


if __name__ == '__main__':
    data = read_data()
    data = clean_data(data)
    trailing(data, 'Personal consumption expenditures', 4)
    # save_dataframe(data)
