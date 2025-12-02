print("Enter a Four Numbers")
a=input()
b=input()
c=input()
d=input()
big=0

if(a>b and a>c and a>d):
    big=a
elif(b>a and b>c and b>d):
    big=b
elif(c>a and c>b and c>d):
    big=c
else:
    big=d
    
print("Biggest Number is :",big)
    