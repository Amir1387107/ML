import numpy as np
import pandas as pd

my_Series=pd.Series([1,2,3,4,5],index=["row1","row2","row3","row4","row5"])
# print(my_Series)
# print(my_Series.values)
# print(my_Series.index)
# print(my_Series.row3),print(my_Series["row3"])
# print(my_Series[my_Series>=3])
# my_Series=my_Series.rename({"row1":"a","row2":"b","row3":"c","row4":"d","row5":"e"})
# print(my_Series)

myarray=np.array([[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]])
myDF=pd.DataFrame(myarray,index=["row1","row2","row3","row4"],columns=["col1","col2","col3","col4"])
# print(myDF)

myDict={"col1":[1,2,3,4],"col2":[5,6,7,8],"col3":[9,10,11,12],"col4":[13,14,15,16]}
myDF2=pd.DataFrame(myDict,index=["row1","row2","row3","row4"])
# print(myDF2)
# print(myDF2.index)
# print(myDF2.columns)
# print(myDF2.values)
# print(myDF2.loc["row1"]["col2"])
# print(myDF2.iloc[0][1])
myDF2["col5"]=[20,21,22,23]
myDF2.loc[["row1","row4"],["col1","col5"]]=0
myDF2.reset_index(drop=True,inplace=True)
myDF2.drop("col2",axis=1,inplace=True)
myDF2.drop(2,axis=0,inplace=True)
myDF2.rename(columns={"col4":"c4"},inplace=True)
myDF2.replace(0,1,inplace=True)

# myDF2.col1=['{:.2f}'.format(x) for x in myDF2.iloc[:,0]]
myDF2["col1"]=myDF2["col1"].apply(lambda x:'{:.2f}'.format(x) )

myDF2.sort_index(axis=0,ascending=True, inplace=True)
myDF2.sort_values(by="c4",ascending=True,inplace=True)

# print(myDF2)
# print(myDF2.head(1))
# print(myDF2.tail(1))

data=pd.read_csv("smartphones.csv")
print(data)