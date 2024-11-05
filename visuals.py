""" For visualizing the data sets """
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def scatter_plots_all(df, label_column, ignore_columns=None):
    cols = list(df.columns)
    cols.remove(label_column)
    cols = [col for col in cols if col not in ignore_columns]
    print(cols)

    for i in range(0, len(cols)-1):
        col_one = cols[i]
        for j in range(i+1, len(cols)):
            col_two = cols[j]
            title = f"{col_one} vs {col_two}"
            sns.scatterplot(data=df, x=col_one, y=col_two, hue=label_column).set_title(title)
            plt.show()


if __name__ == '__main__':
    data = pd.read_csv('Data/High_Corr_Features_Labeled_normalized.csv.csv')
    scatter_plots_all(data, 'Label', ignore_columns='Gross domestic product')
