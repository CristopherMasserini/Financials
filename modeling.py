"""
File for building out models
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def keep_columns(df, columns_keep, label):
    data_columns = list(df.columns)
    for col in data_columns:
        if col not in columns_keep and col != label:
            df = df.drop(col, axis=1)

    return df


def knn_model(df, label, neighbors=3):
    X = df.drop(label, axis=1)
    y = df[label]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Scale the features using StandardScaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy


def k_means_model():
    pass


def best_n(df, label, n_max=10):
    neighbors = []
    accuracies = []
    for i in range(1, n_max+1):
        accuracy = knn_model(df, label, neighbors=i)
        neighbors.append(i)
        accuracies.append(accuracy)
        print(f"{i} neighbors: {accuracy}")


if __name__ == '__main__':
    data = pd.read_csv('Data/High_Corr_Features_Labeled_normalized.csv')
    data_cleaned = keep_columns(data,
                                ['Personal consumption expenditures', 'Gross private domestic investment'],
                                'Label')
    best_n(data_cleaned, 'Label', 10)
    # knn_model(data_cleaned, 'Label')
