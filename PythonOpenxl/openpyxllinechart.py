from openpyxl import Workbook
from openpyxl.chart import LineChart,Reference
workbook=Workbook()
sheet=workbook.active
rows=[
    ["Year","Sales"],
    [2010,3000],
    [2011,4000],
    [2012,5000],
    [2013,4333],
    [2014,6000],
    [2015,5000],
    [2016,7000],
]
for row in rows:
    sheet.append(row)
chart=LineChart()
data = Reference(worksheet=sheet,
               min_row=1,
               max_row=8,
               min_col=2,
               max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
workbook.save("..//data//linechart.xlsx")

