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


if __name__ == '__main__':
    data = pd.read_csv('Data/High_Corr_Features_Labeled.csv')
    comps = 5
    # pca(data, 'Label', comps)
    data_PCA = pca(data, 'Label', comps)
    data_PCA.to_csv(f'Data/High_Corr_Features_PCA{comps}.csv', index=False)
