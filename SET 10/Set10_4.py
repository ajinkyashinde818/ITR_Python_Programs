import array
a = array.array("i",[1,2,3,4,5,6,7,8,9])
print("Array is :",a)
sum = 0

for i in range (len(a)):
    sum = sum+ a[i]
    
print("Sum Of thr Array : ",sum)