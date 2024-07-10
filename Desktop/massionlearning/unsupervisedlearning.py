import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans



iris=load_iris()
x=iris.data

kmn=KMeans(n_clusters=3)
kmn.fit(x)
lable=kmn.predict(x)

center=kmn.cluster_centers_


# plt.scatter(x[:,0],x[:,2],c=lable)
# plt.scatter(center[:,0],center[:,2],marker="*",s=150)
# plt.show()

# print(kmn.inertia_)

y=[]

for k in range(1,6):
    kmn=KMeans(n_clusters=k)
    kmn.fit(x)
    y.append(kmn.inertia_)

print(y)

plt.plot(np.arange(1,6),y,ls="-",marker="o")
plt.xlabel("number of cluster")
plt.ylabel("inertia")

plt.show()




