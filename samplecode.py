import random
def createship():
rows=random.randint(1,8)
col=random.randint(1,8)
x=random.randint(0,1)

if x==0:
vertical_ship = [[rows+1,col] ,[rows,col] , [rows+1,col]]

else:
horizontal_ship= [rows,col+1], [rows,col] , [rows,col+1]

