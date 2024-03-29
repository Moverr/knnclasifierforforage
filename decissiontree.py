# import mglearn as mglearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
cancer = load_breast_cancer()

x_train,x_test,y_train, y_test = train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state= 42)\


tree = DecisionTreeClassifier(random_state=0,max_depth=4)
tree.fit(x_train,y_train)

print("Accurancy of the Classifier {} \n :".format(tree.score(x_train,y_train)))
print(" Accurancy on Training Test {} ]\n ".format(tree.score(x_test,y_test)))

export_graphviz(tree,out_file="tree.dot",class_names=["malignant","benign"], feature_names=cancer.feature_names,impurity=False,filled=True)