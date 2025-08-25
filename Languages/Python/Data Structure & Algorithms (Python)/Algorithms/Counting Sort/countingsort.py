""" Counting Sort """

# 1. A 'countingSort' method that recives an array of integers
def countingSort(arr):
    # 2. An array inside the mthod to keep count of teh values
    max_val = max(arr)
    count = [0] * max(max_val + 1)
    
    # 3. A loop inside the method that counts and removes values, by incrementing elements in the counting array.
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    # 4. A loop inside the method that recreates the array by using the counting array, so that the elements appear in the right order.
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
    
    return arr

# 5. An array with values to sort
mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortedlist = countingSort(mylist)
print(mysortedlist)
