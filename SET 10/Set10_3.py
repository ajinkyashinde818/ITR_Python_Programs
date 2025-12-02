import array
a = array.array("i",[1,2,3,4,5,6,7,8,9])
print("Array is :",a)
print("Appending 20,30 ")
a.append(20)
a.append(30)
print("Array is :",a)

print("Inserting 10, 11")
a.insert(0, 10)
a.insert(4, 11)
print("Array is :",a)

print("Removing the 7")
a.remove(7)
print("Array is :",a)