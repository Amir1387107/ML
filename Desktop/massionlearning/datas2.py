import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing as pr
from sklearn.preprocessing import scale , normalize , minmax_scale


mydata=pd.read_csv("mydata.csv")

# print(mydata.duplicated())
mydata.drop_duplicates(inplace=True)
mydata.drop_duplicates(["columns2"],inplace=True)


my_source1=pd.read_csv("my_source1.csv")
my_source2=pd.read_csv("my_source2.csv")

my_concat=pd.concat([my_source1,my_source2],axis=0,ignore_index=True)

my_concat.drop(["4"],axis=1,inplace=True)
my_concat.drop_duplicates(inplace=True)

smartphones=pd.read_csv("smartphones.csv")

# print(smartphones.describe())
# print(smartphones.OS.value_counts())

cat_os=smartphones.groupby(smartphones["OS"])

# print(cat_os.head(20))
# print(cat_os.mean())


# print(pd.crosstab(smartphones.OS,smartphones.Capacity))

# print(pd.pivot_table(smartphones,index="Name",columns="Company",values="Ram"))

smartphones.rename(index=smartphones.Name,inplace=True)
smartphones.drop(["Name","Company"],axis=1,inplace=True)

smartphones_data=pd.get_dummies(smartphones,dtype=int)
# smartphones_data.drop(["OS_windows"],axis=1,inplace=True)

scale_data=scale(smartphones_data)

df_smartphones=pd.DataFrame(scale_data,index=smartphones_data.index,columns=smartphones_data.columns) #this is standard with the mean of 0 in each column

norm_data=normalize(smartphones_data,norm="l2",axis=0)

df2_smartphones=pd.DataFrame(norm_data,index=smartphones_data.index,columns=smartphones_data.columns) #this is standard with the mean of 0 in each column

norm2_data=normalize(smartphones_data,norm="l1",axis=0)

df3_smartphones=pd.DataFrame(norm2_data,index=smartphones_data.index,columns=smartphones_data.columns) #this is standard with the mean of 0 in each column


minmax_df=minmax_scale(smartphones_data,feature_range=(0,100))
df4_smartphones=pd.DataFrame(minmax_df,index=smartphones_data.index,columns=smartphones_data.columns) #this is standard with the mean of 0 in each column

# print(df4_smartphones)



df=pd.DataFrame(pd.array([1,2,3,4,10,27]))
# print(df.quantile(0.5))   #0.5=mean, 0.25=Q1 ,0.75=Q2

df.boxplot()
plt.show()  #from this we undrestand 27 is an outlier


