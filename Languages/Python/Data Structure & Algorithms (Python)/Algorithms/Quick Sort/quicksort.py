""" Simple Quick Sort """

# A partition method that recives a sub-array, moves values around, swaps the pivot element into sub-array and reutrns the index where the next split in sub-arrays happens.
def partition(array, low, high):
    """" Partition Method """
    pivot: int = array[high]
    i = low - 1

    for j in range (low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

# A quicksort method that calls itself (recurssion) if the sub-array has a size larger than 1.
def quicksort(array, low = 0, high=None):
    """ Quick Sort Method """
    if high is None:
        high: int = len(array) - 1

    if low < high:
        pivot_index: int = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

# An array with values to sort
mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)
