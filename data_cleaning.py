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
    return df


def save_dataframe(df):
    # Plotting done in Tableau at:
    # https://public.tableau.com/app/profile/cristopher.masserini/viz/Financials_17284199840920/Sheet1
    df.to_csv('Data/GDP_data_cleaned.csv')


if __name__ == '__main__':
    df = read_data()
    df = clean_data(df)
    save_dataframe(df)
