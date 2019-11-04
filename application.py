import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import mglearn

 

def importDataset( url, names):
    dataset = pd.read_csv(url, usecols=[0, 1, 2], names=names)
    return dataset

def importResultsDataset( url, names):
    resultdataset = pd.read_csv(url, usecols=[3], names=names)
    return resultdataset

def splitTrainingData(dataset,resultdataset):
    x_train, x_test, y_train, y_test = train_test_split(dataset,resultdataset,random_state = 0)
    return  x_train, x_test, y_train, y_test

def knnClassifier(dataset,resultdataset,newdataset):
    x_train, x_test, y_train, y_test =  splitTrainingData(dataset,resultdataset)
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train, y_train)
    
    result  = knn.predict(newdataset)
    x,y = mglearn.datasets.make_forge()

    mglearn.discrete_scatter(x[:,0],x[:,1],y)

    # print("ASK {} ".format(y_test))
    # print("Test result : {} ".format(knn.score(y_test,x_test)))
    return result

def main():
    names = ['Height', 'Weight', 'Gender']
    resultnames = ['AgeGroup']

    dataseturl = "./dataset.csv"
    dataset = importDataset(dataseturl, names)
    resultdataset =  importResultsDataset(dataseturl,resultnames)

    print("Data set \n {} ".format(dataset[:10]))

    print("Result data set \n {} ".format(resultdataset[:20]))

    newDataset = np.array([[161.29, 48.987936, 1]])
    result  = knnClassifier(dataset,resultdataset,newDataset)    
    targetNames = np.array(['child','Teen','Adult'])  
    print("Result : {} ".format(targetNames[result]))



    newDataset = np.array([[113.665, 17.463292, 1]])
    result  = knnClassifier(dataset,resultdataset,newDataset)     
    print("Result : {} ".format(targetNames[result]))

    


 
 
main()
