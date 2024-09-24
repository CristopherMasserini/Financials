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


def plot_columns(df, col1, col2):
    plt.plot(col1, col2)
    plt.show()

