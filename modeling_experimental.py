# Assumes the submodule https://github.com/CristopherMasserini/PenalizedKNN.git is added.
from PenalizedKNN import Data, Model


def modeling(file, nclassifiers):
    dataset = Data.DataSet()
    model = Model.KNNPenalized(nclassifiers)
    dataset.dataframe_to_dataset(file, 'Label')
    model.test_model(dataset, 0.2, ["0", "1", "2", "3"])


if __name__ == '__main__':
    modeling('Files/High_Corr_Features_Reduced.csv', 3)
