"""
File for building out models
"""

from random import randint
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


def keep_columns(df, columns_keep, label):
    data_columns = list(df.columns)
    for col in data_columns:
        if col not in columns_keep and col != label:
            df = df.drop(col, axis=1)

    return df


def get_train_test(df, label, scale=True):
    X = df.drop(label, axis=1)
    y = df[label]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    if scale:
        # Scale the features using StandardScaler
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test


def knn_model(df, label, neighbors=3):
    X_train, X_test, y_train, y_test = get_train_test(df, label)

    knn = KNeighborsClassifier(neighbors)
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


def random_forest(df, label):
    X_train, X_test, y_train, y_test = get_train_test(df, label)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)
    return accuracy


def random_forest_hyperparameter_tuning(df, label, attempts):
    param_dist = {'n_estimators': randint(20, 500),
                  'max_depth': randint(1, 40)}

    X_train, X_test, y_train, y_test = get_train_test(df, label)
    model = RandomForestClassifier()

    # Use random search for hyperparameter tuning
    rand_search = RandomizedSearchCV(model,
                                     param_distributions=param_dist,
                                     n_iter=attempts)

    rand_search.fit(X_train, y_train)
    best_model = rand_search.best_estimator_

    # Best hyperparameters
    print('Best hyperparameters:', rand_search.best_params_)


if __name__ == '__main__':
    # KNN
    # data = pd.read_csv('Files/High_Corr_Features_PCA5.csv')
    # data_cleaned = keep_columns(data, ['comp1', 'comp3'], 'Label')
    #
    # best_n(data_cleaned, 'Label', 10)

    # Random Forest
    data_rf = pd.read_csv('Files/High_Corr_Features_Reduced.csv')
    random_forest_hyperparameter_tuning(data_rf, 'Label', 5)
    # random_forest(data_rf, 'Label')
