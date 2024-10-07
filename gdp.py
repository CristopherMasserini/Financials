"""
GDP data can be found: https://bea.gov/itable/national-gdp-and-personal-income
"""

import pandas as pd
import matplotlib.pyplot as plt


def read_data():
    data = pd.read_csv('Data/GDP_data.csv')

    # Remove: Change in private inventories, Net exports of goods and services, Addendum:
    df = data.drop(columns='Change in private inventories')
    df = df.drop(columns='Net exports of goods and services')
    df = df.drop(columns='Addendum:')

    return df


def concat_year_quarter(df):
    df['Year Quarter'] = df['Year'].astype(str) + df['Quarter'].astype(str)
    return df

def plot_columns(df, col1, col2):
    x = df.loc[:, col1]
    y = df.loc[:, col2]
    plt.plot(x, y)
    plt.show()


def run():
    df = read_data()
    concat_year_quarter(df)
    # print(concat_year_quarter(df))
    # plot_columns(df, 'Year', 'Personal consumption expenditures')

run()
