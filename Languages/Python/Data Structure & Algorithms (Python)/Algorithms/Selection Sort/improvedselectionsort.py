""" Improved Selection Sort """

# Create array list
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
# Outer Loop
for i in range(n):
    min_index = i

    # Inner Loop
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    
    # Switch places
    mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

print(mylist)
