from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass()
class people():
    name:str
    num:int
    age:int=0
p=[people('steve',1,23),people('Raju',2,34),people("Rahul",3,25)]
data=[[p.name,p.num,p.age]for p in p]
data=[['Name','Num','Age']]+data
for d in data:
    sheet.append(d)
    wb.save("../data//dtclassdemo.xlsx")

