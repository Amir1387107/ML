import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

from sklearn.cluster import MeanShift


iris=load_iris()
x=iris.data

ms=MeanShift(bandwidth=0.85)
ms.fit(x)

labels=ms.labels_
center=ms.cluster_centers_


plt.scatter(x[:,0],x[:,2],c=labels)
plt.scatter(center[:,0],center[:,2],marker="X",s=150,linewidths=5)

plt.show()


