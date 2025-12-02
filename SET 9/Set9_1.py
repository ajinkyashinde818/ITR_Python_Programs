N=5
x=[2,3,5,7,9]
y=[4,5,7,10,15]
Sumxy,Sumx,Sumy,Sumx2=0,0,0,0
for i in range(0,5):
    Sumxy=Sumxy+(x[i]*y[i])
    Sumx=Sumx+x[i]
    Sumy=Sumy+y[i]
    Sumx2=Sumx2+(x[i]*x[i])
print("SUMXY=",Sumxy) 
print("SUMX=",Sumx)
print("SUMY=",Sumy)
print("SUMX2=",Sumx2)   
    
mnr=N*Sumxy-(Sumx*Sumy)
mdr=N*Sumx2-(Sumx*Sumx)
M=mnr/mdr
print("Slope(M)=",M)

B=(Sumy-M*Sumx)/N
print('Intercept(B)=',B)

no_Sunshine=8
Y=M*no_Sunshine+B
print("No of ICE creams that may be soldif Sunshine is for",no_Sunshine,"hours is ",Y)
