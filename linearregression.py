import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
  
# import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LinearRegression

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
# print("{}".format(cancer))
x_train,x_test,y_train, y_test = train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state= 42)