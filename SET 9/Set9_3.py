n =10
count = 0
num = 2 
while(count<n):
    flag = True
    for i in range(2,num):
        if num%i==0:
            flag = False
            break
    if flag:
        print(num,",",end = " ")
        count+=1
    num+=1
         
