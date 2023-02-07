
import pandas as pd
import numpy as np
data1=pd.read_excel("d://data/cmpdata.xlsx",sheet_name="Sheet1")
data2=pd.read_excel("d://data/cmpdata.xlsx",sheet_name="Sheet2")
print(data1)
print(data2)
data1['price_1']=np.where(data1['price'],0,data2['price']-data1['price'])
print(data1.to_html("demo.html"))