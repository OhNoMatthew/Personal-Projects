""" Merge Sort (Recurssion) """

# 1. A function that takes an array, splits it in two, and calls itself with each half of that array so that the arrays are split again and again recursively, until a sub-array only consist of one value.
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
  
    mid = len(arr) // 2
    leftHalf: list = arr[:mid]
    rightHalf: list = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

# 2. Another function that merges the sub-arrays back together in a sorted way.
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 3. An array with values that needs to be sorted.
mylist: list = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print('Sorted Array: ', mysortedlist)