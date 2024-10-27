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


def trailing_feature(df, col, quarters=4, all_features=False):
    # Trailing average of previous x quarters
    col_name = f'{col}_average{quarters}quarters'
    col_data = df.loc[:, col]
    trailing_quarter_averages = []

    init_trail_range = list(range(0, quarters))
    for i in range(0, len(df.loc[quarters:, 'Year Quarter'])):
        sum = 0
        for j in init_trail_range:
            sum += col_data[j]
        trailing_quarter_averages.append(sum / 4)

        init_trail_range = [x + 1 for x in init_trail_range]

    if not all_features:
        dataNew = {'Year Quarter': df.loc[quarters:, 'Year Quarter'],
                   'GDP': df.loc[quarters:, 'Gross domestic product'],
                   'GDP, current dollars': df.loc[quarters:, 'Gross domestic product, current dollars'],
                   col_name: trailing_quarter_averages}
        pd.DataFrame(dataNew).to_csv(f'Data/{col}_trailing{quarters}quarters.csv', index=False)
    else:
        return col_name, trailing_quarter_averages


def trailing_all_features(df, quarters=4):
    cols = df.columns
    cols = cols.drop(['Gross domestic product', 'Gross domestic product, current dollars', 'Year Quarter'])
    dataNew = {'Year Quarter': df.loc[quarters:, 'Year Quarter'],
               'GDP': df.loc[quarters:, 'Gross domestic product'],
               'GDP, current dollars': df.loc[quarters:, 'Gross domestic product, current dollars']}
    for col in cols:
        averages = trailing_feature(df, col, quarters, True)
        dataNew['col'] = averages

    pd.DataFrame(dataNew).to_csv(f'Data/AllFeatures_tailing{quarters}quarters.csv', index=False)


if __name__ == '__main__':
    data = read_data()
    data = clean_data(data)
    trailing_feature(data, 'Personal consumption expenditures', 4)
    # save_dataframe(data)
