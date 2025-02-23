"""
File for exploring the data for trends to be used in modeling
"""

import data_cleaning as dc
import pandas as pd
import numpy as np


def run_correlations_GDP(df):
    # Ignore Year, Quarter
    # Use Gross domestic product vs everything else
    cols = df.columns
    cols = cols.drop(['Gross domestic product', 'Gross domestic product, current dollars', 'Year Quarter'])
    corr_data = {'Feature': [], 'Corr_GDP': [], 'Corr_GDP_CD': []}
    for col in cols:
        corr_GDP = df['Gross domestic product'].corr(df[col])
        corr_GDP_CD = df['Gross domestic product, current dollars'].corr(df[col])
        corr_data['Feature'].append(col)
        corr_data['Corr_GDP'].append(corr_GDP)
        corr_data['Corr_GDP_CD'].append(corr_GDP_CD)

    pd.DataFrame(corr_data).to_csv('Files/Feature_Correlation.csv', index=False)


def drop_low_correlation_GDP(dfAll, dfCorr):
    features = list(dfCorr.loc[:, 'Feature'])
    corr_gdp = list(dfCorr.loc[:, 'Corr_GDP'])
    corr_gdp_cd = list(dfCorr.loc[:, 'Corr_GDP_CD'])

    drop_lst = [feature for ind, feature in enumerate(features) if np.abs(corr_gdp[ind]) < 0.5 and np.abs(corr_gdp_cd[ind])]
    dfAll = dfAll.drop(drop_lst, axis=1)
    return dfAll

# Do similar but drop features with high correlation to other features, not just gdp


if __name__ == '__main__':
    data = pd.read_csv('Files/GDP_data_cleaned.csv')
    run_correlations_GDP(data)
    data_corr = pd.read_csv('Files/Feature_Correlation.csv')
    df_high_corr_features = drop_low_correlation_GDP(data, data_corr)
    df_high_corr_features = dc.remove_non_needed_labels(df_high_corr_features)
    df_high_corr_features.to_csv('Files/High_Corr_Features.csv', index=False)

