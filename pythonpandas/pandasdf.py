import pandas  as pd
d={'Team':["India","Australia","Pakistan","Srilanka","England"],
   'Rank':[1,2,3,4,5],
   'Winper':['60%','55%','45%','35%','48%']
   }
df=pd.DataFrame(d)
df.rename(columns={"Rank":"Ranking"},inplace=True)
df.set_axis(df['Team'],inplace=True)
print(df.loc[df['Ranking']>=3])

