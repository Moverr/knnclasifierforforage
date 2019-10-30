import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

x_train, x_test, y_train, y_test = ""

def importDataset( url, names):
    dataset = pd.read_csv(url, usecols=[0, 1, 2], names=names)
    return dataset

def importResultsDataset( url, names):
    resultdataset = pd.read_csv(url, usecols=[3], names=names)
    return resultdataset

def splitTrainingData(dataset,resultdataset):
    x_train, x_test, y_train, y_test = train_test_split(dataset,resultdataset,random_state = 0)
    return  x_train, x_test, y_train, y_test

def knnClassifier():
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train, y_train)
    x_new = np.array([[161.29, 48.987936, 1]])
    return knn.predict(x_new)

def main(self):
    names = ['Height', 'Weight', 'Gender']
    resultnames = ['AgeGroup']

    dataseturl = "./dataset.csv"
    dataset = importDataset(dataseturl, names)
    resultdataset =  importDataset(dataseturl,resultnames)

    print("Data set \n {} ".format(dataset[:10]))

#         print("Result data set \n {} ".format(resultdataset[:20]))


#         print("Panda Version  :  {}".format(pd.__version__))
#         print("Let me know oaea ")


# # split data using sklean
#         prediction = splitTrainingData()

#         # K Nearest Neighborhood

        # ageGroup = np.array(['Child','Teen','Adult'])
        # print(" Prediction {}".format(ageGroup[prediction]))


 
main()
