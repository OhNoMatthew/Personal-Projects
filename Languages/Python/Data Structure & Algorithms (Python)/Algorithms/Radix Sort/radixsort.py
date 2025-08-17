""" Radix Sort """

# 1. An array with non negative integers that needs to be sorted.
mylist = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array: ", mylist)

# 2. A two dimensional array with index 0 to 9 to hold values with the current radix in focus.
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(mylist)
exp = 1

# 3. An outer loop that runs as many times as there are digits in the highest value.
while maxVal // exp > 0:

    # 4. A loop that takes values from the unsorted array and places them in the correct postion in the dimensional radix array.
    while len(mylist) > 0:
        val = mylist.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)
    
    # 5. A loop that puts values back into the initial array from the radix array.
    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            mylist.append(val)
    
    exp *= 10

print(mylist)
