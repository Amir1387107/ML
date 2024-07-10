import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


years=[1960,1970,1980,1990,2000,2010,2020]
iranpop=[21.19,28.51,38.67,56.23,66.13,74.75,80.29]
turkeypop=[27.47,34.88,43.98,53.92,63.24,72.33,79.51]

cityname=["Tehran","mashhad","isfahan","karaj","tabriz","shiraz"]
citypop=[7153309,2307177,1547164,1448075,1424641,1249942]

smartphones=pd.read_csv("smartphones.csv")


# plt.plot(years,iranpop)
# plt.xlabel("year")
# plt.ylabel("population")
# plt.yticks([21.19,28.51,38.67,56.23,66.13,74.75,80.29],["21m","28m","38m","56m","66m","74m","80m"])
# # plt.show()

# plt.scatter(years,iranpop)
# # plt.show()

# plt.hist(citypop,bins="auto")    #برای پیدا کردن بهترین bins باید جزر تعداد داده هارا بگیریم و رند کنیم
# # plt.show()

# plt.figure(dpi=100,figsize=(11,8))
# plt.pie(citypop,labels=cityname)
# # plt.show()


# popsize=np.array(citypop)/10000
# colors=["violet","green","orange","tomato","blue","pink"]
# plt.scatter(np.arange(6),citypop,s=popsize,c=colors)
# plt.title("Iran pollution")
# plt.xticks([0,1,2,3,4,5],cityname)
# plt.margins(0.1)
# plt.yticks([1000000,2000000,3000000,4000000,5000000,6000000,7000000],["1m","2m","3m","4m","5m","6m","7m"])
# plt.text(-0.25,7153309,"Iran Capital",fontsize=5)
# plt.show()


# plt.plot(years,iranpop,ls="-",marker="+",mew=8)
# plt.plot(years,turkeypop,ls="--",marker="+",lw=1)
# plt.title("Iran vs Turkey")
# plt.xlabel("year")
# plt.ylabel("population")
# plt.legend(["Iran","Turkey"],loc="best")
# plt.yticks([20,30,40,50,60,70,80],["2m","3m","4m","5m","6m","7m","8m"])
# plt.grid()
# plt.annotate("Iran in 1990",xytext=(1990,40),xy=(1990,56.23),arrowprops={'facecolor':"c","width":4},fontsize=10,font="Times New Roman")

# plt.show()

# plt.subplot(1,2,1)
# plt.plot(years,iranpop)
# plt.xlabel("year")
# # plt.ylabel("population")
# plt.margins(0.1)
# plt.title("Iran Pop")
# plt.yticks([20,30,40,50,60,70,80],["2m","3m","4m","5m","6m","7m","8m"])

# plt.subplot(1,2,2)
# plt.plot(years,turkeypop)
# plt.xlabel("year")
# # plt.ylabel("population")
# plt.margins(0.1)
# plt.title("Turkey Pop")
# plt.yticks([20,30,40,50,60,70,80],["2m","3m","4m","5m","6m","7m","8m"])

# plt.show()

# #sb.stripplot(x="OS",y="Capacity",data=smartphones,size=10)
# sb.swarmplot(x="OS",y="Capacity",data=smartphones,size=10,hue="Company")
# plt.show()



# sb.boxenplot(x="Company",y="Ram",data=smartphones)
# plt.show()


# sb.jointplot(data=smartphones,x="Capacity",y="Ram",kind="scatter")
sb.pairplot(data=smartphones,hue="Name",palette="hls",plot_kws={"s":80})


plt.show()
