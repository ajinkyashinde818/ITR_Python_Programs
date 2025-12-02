
arr = [2, -4, 0, 7, -1, 0, 9, -3]

pc = 0
nc = 0
zero_count = 0

for num in arr:
    if num > 0:
        pc += 1
    elif num < 0:
        nc += 1
    else:
        zero_count += 1

print("Array:", arr)
print("Positive numbers:", pc)
print("Negative numbers:", nc)
print("Zeros:", zero_count)
