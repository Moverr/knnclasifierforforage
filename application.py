import pandas as pd

class Application:
    def __init__(self):
        pass
    def importDataset(self,url):
        pass

    def main(self):
        dataseturl = "./dataset.csv"
        names = ['Height', 'Weight', 'Age', 'Gender']
        dataset = pd.read_csv(dataseturl, names=names)


        print("Panda Version  :  {}".format(pd.__version__))
        print("Let me know oaea ")



p1 = Application()

p1.main()