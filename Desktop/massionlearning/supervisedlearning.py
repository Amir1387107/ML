from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier as KNC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR



iris=datasets.load_iris()

# print(iris.feature_names)
# print(iris.data.shape)
# print(iris.target_names)
# print(iris.DESCR)

# print(iris.data)


iris_df=pd.DataFrame(iris.data,columns=iris.feature_names)
iris_df["target"]=iris.target


# pd.plotting.scatter_matrix(iris_df,c=iris.target,s=150,figsize=[11,11])
# plt.show()

# x=iris.data[:,[2,3]]
# y=iris.target

# plt.scatter(x[:,0],x[:,1],c=y)
# plt.show()


x=iris.data
y=iris.target


knn=KNC(n_neighbors=6,metric="minkowski",p=2)
knn.fit(x,y)

y_predict=knn.predict(np.array([[5,3,1,0.2]]))

# print(y_predict)

x_train,x_test,y_train,y_test=tts(x,y,test_size=0.333,random_state=42,stratify=iris.target)

knn=KNC(n_neighbors=5,metric="minkowski",p=2)
knn.fit(x_train,y_train)

how_much_correct=knn.score(x_test,y_test)

# print(how_much_correct)

# neighbors=np.arange(1,30)
# train_accuracy=np.empty(len(neighbors))
# test_accuracy=np.empty(len(neighbors))
# for i,k in enumerate(neighbors):
#     knn_model=KNC(n_neighbors=k)
#     knn_model.fit(x_train,y_train)
#     train_accuracy[i]=knn_model.score(x_train,y_train)
#     test_accuracy[i]=knn_model.score(x_test,y_test)

# plt.plot(neighbors,train_accuracy,label="train accuracy")
# plt.plot(neighbors,test_accuracy,label="test accuracy")
# plt.legend()
# plt.xlabel("number of neighbors")
# plt.ylabel("accuracy")

# plt.show()





