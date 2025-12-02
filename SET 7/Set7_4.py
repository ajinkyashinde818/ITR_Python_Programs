salary=int(input("Enter a Salary:"))



if (salary>0 and salary<15000):
    print("Peon")
elif(salary >15001 and salary<25000):
    print("2nd Division Cleark")
elif(salary >25001 and salary<35000):
    print("1st Division cleark")
elif(salary >35001 and salary<45000):
    print("Assistant Manager")
elif(salary >45001 and salary<60000):
    print("Manager")
else:
    print("Invalid Input")
