import numpy as np
import pandas as pd
from sklearn import datasets
from scipy.stats import randint
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import roc_auc_score


from sklearn.naive_bayes import GaussianNB



bcd=datasets.load_breast_cancer()

x=bcd.data
y=bcd.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# p_grid={"n_neighbors":np.arange(1,50)}

# knn=KNeighborsClassifier()
# knn_cv=GridSearchCV(knn,p_grid,cv=5)
# knn_cv.fit(x,y)

# print(knn_cv.best_params_)
# print(knn_cv.best_score_)




# params={"max_depth":[None,3],"max_features":randint(1,9),"min_samples_leaf":randint(1,9)}

# tree=DecisionTreeClassifier()
# tree_cv=RandomizedSearchCV(tree,params,cv=169)
# tree_cv.fit(x_train,y_train)

# print(tree_cv.best_params_)
# print(tree_cv.best_score_)

# score=tree_cv.score(x_test,y_test)

# print(score)


gnb=GaussianNB()

y_pred=gnb.fit(x_train,y_train).predict(x_test)

# print(gnb.score(x_test,y_test))

ras=roc_auc_score(y_test,y_pred)

print(ras)
