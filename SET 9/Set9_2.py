x=[18,25,57,45,26,64,37,40,24,33]
y=[15000,29000,68000,52000,32000,80000,41000,45000,26000,33000]
N=10
Sumx,Sumy,Sumxy,Sumx2,Sumy2=0,0,0,0,0
for i in range(10):
    Sumx=Sumx+x[i]
    Sumy=Sumy+y[i]
    Sumxy=Sumxy+(x[i]*y[i])
    Sumx2=Sumx2+(x[i]*x[i])
    Sumy2=Sumy2+(y[i]*y[i])

import math
Value1=(Sumx*Sumy)/N 
nr=Sumxy-Value1
Value2=Sumx2-((Sumx**2)/N)
Value2=math.sqrt(Value2)

Value3=Sumy2-((Sumy**2)/N)
Value3=math.sqrt(Value3)
pc=nr/(Value2*Value3)
print("Correlation between Age and Sallary is",pc)
    
    