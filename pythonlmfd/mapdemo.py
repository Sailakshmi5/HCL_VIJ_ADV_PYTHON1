old_price=[23,4,5,80,2,60,60,69,70,85,90]
rs=5
def add_price(no):
    return no+5
new_price=map(add_price,old_price)
new_price1=list(map(lambda  n:n+rs,old_price))
print(list(new_price1))
