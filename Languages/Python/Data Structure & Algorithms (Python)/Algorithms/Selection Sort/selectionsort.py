""" Simple Selection Sort """

# 1. An array with values to sort
mylist: list = [64, 34, 25, 5, 22, 11, 90, 12]

n: int = len(mylist)

# 2. An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.
for i in range(n-1):
    min_index = i

    # 3. An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j

    # Remove the value and insert it to the front.
    min_value = mylist.pop(min_index)
    mylist.insert(i, min_value)

print(mylist)

# This has a shifting problem as the lowest value is removed from the array and inserted back into the array at the first index.
