"""
File for reducing features for modeling the data
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def pca(df, label, components):
    cols_non_label = [col for col in df.columns if col != label]
    features = df.loc[:, cols_non_label]
    labels = df.loc[:, label]
    features = StandardScaler().fit_transform(features)
    pca_res = PCA(n_components=components)

    principalComponents = pca_res.fit_transform(features)
    columns_df = [f'comp{i}' for i in range(1, components + 1)]
    pcaDF = pd.DataFrame(data=principalComponents, columns=[columns_df])
    pcaDF[label] = labels
    print(pca_res.explained_variance_ratio_)
    return pcaDF


def lasso(df):
    pass


def low_variance_filter(df, label, var_threshold=10):
    cols_non_label = [col for col in df.columns if col != label]
    new_columns = [label]
    for col in cols_non_label:
        column_variance = df.loc[:, col].var()
        if column_variance > var_threshold:
            new_columns.append(col)

    return df.loc[:, new_columns]


if __name__ == '__main__':
    comps = 3
    var_min = 20
    data = pd.read_csv('Data/High_Corr_Features_Labeled.csv')

    data_high_var = low_variance_filter(data, 'Label', var_min)
    data_PCA = pca(data_high_var, 'Label', comps)
    data_PCA.to_csv(f'Data/High_Corr_Features_Reduced.csv', index=False)
