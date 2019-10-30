import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.neighbors  import KNeighborsClassifier
import numpy as np



class Application:
    def __init__(self):
        self.names = ['Height', 'Weight', 'Gender']
        self.resultnames = ['AgeGroup']
         
    def importDataset(self,url,names):
        self.dataset = pd.read_csv(url,usecols=[0,1,2], names=names)

    def importResultsDataset(self,url,names):
        self.resultdataset = pd.read_csv(url,usecols=[3], names=names)
    
    def splitTrainingData(self):
        self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(self.dataset,self.resultdataset,random_state = 0)



    def main(self):
        dataseturl = "./dataset.csv"
        self.importDataset(dataseturl,self.names)
        self.importDataset(dataseturl,self.resultnames)
        
 
        print("Data set \n {} ".format(self.dataset[:10]))

        print("Result data set \n {} ".format(self.resultdataset[:20]))
        

        print("Panda Version  :  {}".format(pd.__version__))
        print("Let me know oaea ")


# split data using sklean
        x_train,x_test,y_train,y_test = train_test_split(dataset,resultdataset,random_state = 0)

        # K Nearest Neighborhood 
        knn = KNeighborsClassifier(n_neighbors = 1)

        knn.fit(x_train,y_train)

        x_new = np.array([[161.29,48.987936,1]])
        
        prediction  = knn.predict(x_new)


        ageGroup = np.array(['Child','Teen','Adult'])
        print(" Prediction {}".format(ageGroup[prediction]))




  




p1 = Application()

p1.main()