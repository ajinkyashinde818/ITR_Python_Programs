def getArithemeticOperation(a,b):
    sum = a + b
    diff = a - b 
    div = a / b
    pro = a * b
    return sum,diff,div,pro
a = int(input("Enter Value for a : "))
b = int(input("Enter Value for b : "))
r1,r2,r3,r4 = getArithemeticOperation(a, b)
print("Addition is ",r1)
print("Substraction is ",r2)
print("Division is ",r3)
print("Multiplication is ",r4)
    

