import pandas as pd
data=pd.read_csv("..//data/tips.csv")
#print(pd.crosstab(index=data['sex'],columns=data['smoker']))
day_wise=data.filter(['tip','day'])
print(day_wise.groupby('day').sum())