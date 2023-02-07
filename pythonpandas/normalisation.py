import pandas as pd
data=pd.read_csv("..//data/tips.csv")
#print(data.isna().any())
#print(data.isna().sum())
tips_male_fm=data.filter(['tip','sex'])
#print(tips_male_fm.groupby('sex').sum())
print(tips_male_fm.sex.value_counts(normalize=True))