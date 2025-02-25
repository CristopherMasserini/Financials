# Assumes the submodule https://github.com/CristopherMasserini/PenalizedKNN.git is added.
from PenalizedKNN.Data import DataSet
from PenalizedKNN.Model import KNNPenalized


def modeling(file, nclassifiers):
    dataset = DataSet()
    model = KNNPenalized(nclassifiers)
    dataset.dataframe_to_dataset(file, 'Label')
    model.test_model(dataset, 0.2, 'Label')


if __name__ == '__main__':
    modeling('Files/High_Corr_Features_Reduced.csv', 3)
