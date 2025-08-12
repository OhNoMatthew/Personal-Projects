""" Binary Search """

mylist: list = [3, 7, 2, 9, 5, 11, 10, 14, 6, 8, 4]
x = 11

def binarySearch(arr, targetVal):
    
    # Initiating left and right.
    left = 0
    right = len(arr) - 1

    # If left value is less or equal to right add them both and divide by 2 to grab the middle postition.
    while left <= right:
        mid = (left + right) // 2

        # If the middle position is the same as the target value return the value.
        if arr[mid] == targetVal:
            return mid
        
        # If the middle position is not the target value, compare to the left value. If the left value is less that the target value then move right.
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1

result = binarySearch(mylist, x)

if result != -1:
    print('Found at index', result)
else:
    print('Not Found')