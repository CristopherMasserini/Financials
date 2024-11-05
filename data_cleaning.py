"""
GDP data can be found: https://bea.gov/itable/national-gdp-and-personal-income
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


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


def remove_non_needed_labels(df):
    df = df.drop(columns=['Gross domestic product, current dollars', 'Year Quarter'])
    return df


def normalize_data(df=None, file_path='', labelName=None):
    # Normalize df to mean 0, std 1
    if file_path:
        df = pd.read_csv(file_path)

    labels = []
    if labelName:
        labels = list(df.loc[:, labelName])
        df = df.drop(columns=[labelName])

    scaler = StandardScaler()
    scaler.fit(df)
    df[df.columns] = scaler.transform(df)

    if labelName:
        df[labelName] = labels

    if file_path:
        df.to_csv(f'{file_path[:-4]}_Standardized.csv', index=False)

    return df


def add_labels(df, col):
    vals = list(df.loc[:, col])
    labels = []

    for val in vals:
        if val < 0:
            labels.append('Contraction')
        elif val == 0:
            labels.append('Flat')
        elif 0 < val <= 2:
            labels.append('Moderate Growth')
        else:
            labels.append('Strong Growth')

    df['Label'] = labels
    df = df.drop(columns=[col])

    return df


if __name__ == '__main__':
    # data = read_data()
    # data = clean_data(data)
    # trailing_feature(data, 'Personal consumption expenditures', 4)
    # save_dataframe(data)
    data = pd.read_csv('Data/High_Corr_Features.csv')
    data = add_labels(data, 'Gross domestic product')
    data = normalize_data(df=data, labelName='Label')
    data.to_csv('Data/High_Corr_Features_Labeled_normalized.csv', index=False)
