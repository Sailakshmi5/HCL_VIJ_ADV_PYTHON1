import pandas as pd
exldata1=pd.read_excel("C://data/exceldata.xlsx",sheet_name='Emp')
print(exldata1)
exldata2=pd.readexcel("C://data/exceldata.xlsx",sheet_name="Department")
print(exldata2)
exdata3=pd.concat([exldata1,exldata2],axis=1,join='inner')
excdata4=pd.merge(left=exldata1,right=exldata2,how='inner')
print(excdata4)
