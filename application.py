import pandas as pd

class Application:
    def __init__(self):
        pass
    def importDataset(self,url):
        pass

    def main(self):
        dataseturl = "./dataset.csv"
        names = ['Height', 'Weight', 'Gender']
        resultnames = ['AgeGroup']
        
        dataset = pd.read_csv(dataseturl,usecols=[0,1,2], names=names)

        # record set 
        resultdataset = pd.read_csv(dataseturl,usecols=[3], names=resultnames)
        
        print("Data set \n {} ".format(dataset[:10]))

        print("Result data set \n {} ".format(resultdataset[:20]))
        

        print("Panda Version  :  {}".format(pd.__version__))
        print("Let me know oaea ")



p1 = Application()

p1.main()