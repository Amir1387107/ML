import numpy as np
import pandas as pd
from sklearn import preprocessing as pr
from sklearn.impute import SimpleImputer


country=pd.read_csv("c_data.csv",header=1)
country.rename(columns={"CountryName":"Name","CountryCode":"Code",
                        "Population growth":"pop_growth","Total population":"pop",
                        "Area (sq. km)":"Area"},inplace=True)
country.drop("Code",axis=1,inplace=True)
country.drop("1",axis=1,inplace=True)
country.rename(index=country.Name,inplace=True)
country.drop("Name",axis=1,inplace=True)

# print(country.info())
# print(country.describe())

maxpop=country["pop"].max
# print(country["pop"][country["pop"]==maxpop])
country.drop("World",axis=0,inplace=True)

# print(country.isnull())

country.replace("?",np.nan,inplace=True)

# print(country)
# print(country.isnull())
# print(country.isnull().sum())
# country.dropna(axis=0,inplace=True)
# country.fillna(0,inplace=True)
# print(country.info())

# country.fillna({"pop_growth":0,"pop":100000,"Area":500000},inplace=True)
# country.fillna(method="ffill",inplace=True)

# i=SimpleImputer(missing_values=np.nan,strategy="mean")
# i.fit(country)

# new_df=i.transform(country)


# print(new_df)


