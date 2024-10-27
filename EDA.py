"""
File for exploring the data for trends to be used in modeling
"""

import pandas as pd


def run_correlations(df):
    # Ignore Year, Quarter
    # Use Gross domestic product vs everything else
    # print(df['Gross domestic product'].corr(df['Personal consumption expenditures']))
    cols = df.columns
    cols = cols.drop(['Gross domestic product', 'Gross domestic product, current dollars', 'Year Quarter'])
    corr_data = {'Feature': [], 'Corr_GDP': [], 'Corr_GDP_CD': []}
    for col in cols:
        corr_GDP = df['Gross domestic product'].corr(df[col])
        corr_GDP_CD = df['Gross domestic product, current dollars'].corr(df[col])
        corr_data['Feature'].append(col)
        corr_data['Corr_GDP'].append(corr_GDP)
        corr_data['Corr_GDP_CD'].append(corr_GDP_CD)

    pd.DataFrame(corr_data).to_csv('Data/Feature_Correlation.csv', index=False)


if __name__ == '__main__':
    data = pd.read_csv('Data/GDP_data_cleaned.csv')
    run_correlations(data)