import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import normalize
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report

from sklearn.neural_network import MLPRegressor



bcd=datasets.load_iris()



x=bcd.data
y=bcd.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


mlp=MLPRegressor(activation="identity",hidden_layer_sizes=(2),solver="sgd",alpha=0.0001,
                 learning_rate_init=0.001,max_iter=500,early_stopping=False)

mlp.fit(x_train,y_train)

score=mlp.score(x_test,y_test)

print(score)



