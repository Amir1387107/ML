import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

from sklearn.cluster import DBSCAN




iris=load_iris()
x=iris.data


dbscan=DBSCAN(eps=0.5,min_samples=5)
dbscan.fit(x)

labels=dbscan.labels_


# plt.scatter(x[:,0],x[:,2],c=labels)
# plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x[:,0],x[:,1],x[:,2],c=labels)

plt.show()