import pandas as pd
df=pd.read_csv('..//data//tested.csv')#load dataset by using read_csv
#print(df)
print(df.shape)
#print(df.isna().any())
df.drop(['Cabin'],axis=1,inplace=True)
df.fillna(method='ffill',inplace=True)
#print(df)
#print(pd.crosstab(
print(df.isna().sum())