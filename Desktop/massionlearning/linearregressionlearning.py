from sklearn.datasets import load_boston
from sklearn.neighbors import KNeighborsClassifier as KNC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge



x=np.arange(1,10)
y=np.array([28,25,26,31,32,29,30,35,36])

x=x.reshape(-1,1) #now this came to columns
y=y.reshape(-1,1) #now this came to columns


# plt.scatter(x,y)
# plt.show()

# reg=LR()
# reg.fit(x,y)

# y_predict=reg.predict(x)

# plt.scatter(x,y)
# plt.plot(x,y_predict)
# plt.show()



boston=load_boston()
boston_df=pd.DataFrame(boston.data,columns=boston.feature_names)
boston_df["price"]=boston.target

x=boston.data
y=boston.target

x_train,x_test,y_train,y_test=tts(x,y,test_size=0.333,random_state=42)

reg=LR()
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)

plt.scatter(y_test,y_pred)
plt.xlabel("price")
plt.ylabel("predict price")
plt.show()

mse=mean_squared_error(y_test,y_pred)

new_x=boston.data[:,[1,2]]
new_y=boston.target

new_x_train,new_x_test,new_y_train,new_y_test=tts(new_x,new_y,test_size=0.333,random_state=42)

new_reg=LR()
new_reg.fit(new_x_train,new_y_train)
new_y_pred=reg.predict(new_x_test)

new_mse=mean_squared_error(new_y_test,new_y_pred)


reg=LR()
cv_score=cross_val_score(reg,boston.data,boston.target,cv=5)

print(np.mean(cv_score))



lasso = Lasso(alpha=0.1,normalize=True)
lasso.fit(boston.data,boston.target)
lasso_coef=lasso.coef_    #this shows you how many features are deleted

plt.plot(range(13),lasso_coef)
plt.xticks(range(13),boston.feature_names)
plt.ylabel("coefficent")
plt.show()


lasso = Lasso(alpha=0.1,normalize=True)
lasso.fit(x_train,y_train)
y_lasso=lasso.predict(x_test)

lasso_mse=mean_squared_error(y_test,y_lasso)


ridge=Ridge(alpha=0.1,normalize=True)
ridge.fit(x_train,y_train)
y_ridge=ridge.predict(x_test)
ridge_mse=mean_squared_error(y_test,y_ridge)



