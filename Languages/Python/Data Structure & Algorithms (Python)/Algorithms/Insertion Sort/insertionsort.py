""" Simple Insertion Sort """

# An array with values to sort
mylist: list = [64, 34, 25, 12, 22, 11, 90, 5]
n: int = len(mylist)

# An outer loop that picks a value to be sorted. 
# For an array with n values, this outer loop skips the first value, and must run n-1 times.
for i in range(1,n):
    insert_index: int = i
    current_value = mylist.pop(i)
    
    # An inner loop that goes through the sorted part of the array, to find where to insert the value.
    # If the value to be sortd is at index i, the sorted part of the array starts at index 0 and ends at index i - 1
    for j in range(i-1, -1, -1):
        if mylist[j] > current_value:
            insert_index: int = j
    mylist.insert(insert_index, current_value)

print(mylist)
