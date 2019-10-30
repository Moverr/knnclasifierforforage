import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.neighbors  import KNeighborsClassifier
import numpy as np



class Application:
    def __init__(self):
        self.names = ['Height', 'Weight', 'Gender']
         
    def importDataset(self,url,names):
        self.dataset = pd.read_csv(url,usecols=[0,1,2], names=names)

         

    def main(self):
        dataseturl = "./dataset.csv"
        self.importDataset(dataseturl,self.names)

        
        resultnames = ['AgeGroup']
        
      

        # record set 
        resultdataset = pd.read_csv(dataseturl,usecols=[3], names=resultnames)
        
        print("Data set \n {} ".format(dataset[:10]))

        print("Result data set \n {} ".format(resultdataset[:20]))
        

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