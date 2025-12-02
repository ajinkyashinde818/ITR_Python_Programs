print("Enter a Numbers")
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print(a)
elif a>c:
    if a>b:
        print(a)
elif b>a:
    if b>c:
        print(b)
elif b>c:
    if b>a:
        print(b)
elif c>a:
    if c>b:
        print(c)
elif c>b:
    if c>a:
        print(c)