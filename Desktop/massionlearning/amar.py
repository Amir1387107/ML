import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats import pearsonr as pr
from scipy.stats import spearmanr as sp
from scipy.stats import chi2_contingency as c2c  #chi_square





smartphones=pd.read_csv("smartphones.csv")
# counts=smartphones.Ram.value_counts()
# category=counts.index
 
# # plt.bar(category,counts)
# # plt.xlabel("Ram")
# # plt.ylabel("counts")
# # plt.xticks([1,2,3,4,5,6,7,8,9])
# # plt.yticks([1,2,3])
# # plt.show()

# def ECDF(data):
#     n=len(data)
#     x=np.sort(data)
#     y=np.arange(1,n+1)/n
#     return x,y

# x,y=ECDF(smartphones.inch)

# # plt.figure(figsize=(10,7))
# # plt.grid()
# # plt.scatter(x,y,s=80)
# # plt.margins(0.05)
# # plt.xlabel("inch",fontsize=15)
# # plt.ylabel("ECDF",fontsize=15)
# # plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

# # plt.show() #in this we  undrestand for example haf of our phones are less than 5.25 inches


# average=np.mean(smartphones.inch)
# median=np.median(smartphones.inch)
# boxplot=np.percentile(smartphones.inch,[25,50,75])

# variance=np.var(smartphones.inch)  #the variance of datas(how far they are from the mean)
# standarddeviation=np.std(smartphones.inch) # the square root of the variance of datas

# covariance=np.cov(smartphones.inch,smartphones.Weight) # show the correlation between these 2 inch and Weight(positive number means the Direct communication and negetive number means reverse communication)

# pearson_coeff , p_value=pr(smartphones.inch,smartphones.Weight) #the coeff part is the same as covariance but it's between -1 and 1


# num_var=smartphones.drop(["Name","Company","Capacity","Ram","OS"],axis=1)
# cor=num_var.corr()  #finding correlation

# # sb.heatmap(cor,yticklabels=cor.columns,xticklabels=cor.columns,vmin=-1,vmax=1) #showing correlation on cahrt or diagram
# # plt.show()


# spearmanr_coeff , p_value=sp(smartphones.Ram,smartphones.Capacity)

table_ob=pd.crosstab(smartphones.Capacity,smartphones.Ram)

chi,p_value,dof,table_ex=c2c(table_ob.values) #very important  



# np.random.seed(42) #makes the numbers the same each time
# rand_np=np.random.random(3)
# win=rand_np>0.5

#better not to run this ...
# for i in range(10):
#     random_num=np.random.random(1000000000)
#     w=random_num>0.5
#     num_head=np.sum(w)/1000000000
#     print(num_head)

sample=np.random.normal(0,1,size=1000000)
sb.displot(sample)

plt.show()


