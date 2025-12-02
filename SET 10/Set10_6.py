import array
a = array.array("i",[12, 45, 7, 89, 23, 5, 77])
print("Array is :",a)


smallest = a[0]
largest = a[0]

for num in a:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Array:", a)
print("Smallest element:", smallest)
print("Largest element:", largest)
