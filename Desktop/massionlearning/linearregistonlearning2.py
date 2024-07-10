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


bcd=datasets.load_breast_cancer()



x=bcd.data
y=bcd.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

knn=KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test)

# print(confusion_matrix(y_test,y_pred))
# print()
# print(classification_report(y_test,y_pred))

lr=LogisticRegression()
lr.fit(x_train,y_train)

y_pred2=lr.predict(x_test)

cm=confusion_matrix(y_test,y_pred2)

cm=normalize(cm,norm="l1",axis=1)

cm_df=pd.DataFrame(cm,columns=bcd.target_names,index=bcd.target_names)


# print(cm_df)

y_pred_prob=lr.predict_proba(x_test)[:,1]

fpr,tpr,thresholds=roc_curve(y_test,y_pred_prob)

# plt.plot([0,1],[0,1],"k--")
# plt.plot(fpr,tpr)
# plt.xlabel("fpr")
# plt.ylabel("tpr")
# plt.show()

ras=roc_auc_score(y_test,y_pred_prob)

print(ras)

