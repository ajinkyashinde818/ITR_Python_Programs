a=12.12
b=12.1
c=32.12
d=32.23
e=11.23
n=5

mean=(a+b+c+d+e)/n

print("Mean :",mean)
import math
v1=math.pow((mean-a),2)
v2=math.pow((mean-b),2)
v3=math.pow((mean-c),2)
v4=math.pow((mean-d),2)
v5=math.pow((mean-e),2)

summation=v1+v2+v3+v4+v5
variation= summation /n
sd=math.sqrt(variation)
print("Standard Deviation :",sd)
minrange=mean-sd
maxrange=mean+sd

print("Min Range :",minrange)
print("Max Range :",maxrange)