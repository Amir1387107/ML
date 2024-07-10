import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

from scipy.cluster.hierarchy import linkage,dendrogram,fcluster


iris=load_iris()
x=iris.data



hirarical=linkage(x,method="complete",)

# dendrogram(hirarical)
# plt.show()

lables=fcluster(hirarical,3,criterion="distance")

print(lables)


plt.scatter(x[:,0],x[:,2],c=lables)
plt.show()




