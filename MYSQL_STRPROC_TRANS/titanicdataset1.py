import pandas as pd
df=pd.read_csv('..//data//tested.csv')#load dataset by using read_csv
print(df.shape)
df.drop(['Cabin'],axis=1,inplace=True)
df.fillna(method='ffill',inplace=True)
print(pd.crosstab(index=df['Sex'],columns=df['Survived']))