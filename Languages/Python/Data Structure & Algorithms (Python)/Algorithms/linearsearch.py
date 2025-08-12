""" Linear Search """

# Time complexity of O(n)

mylist: list = [3, 7, 2, 9, 5, 10, 14, 6, 8, 4]

if 4 in mylist:
    print('Found!')
else:
    print('Not Found!')

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

x = 4

result = linearSearch(mylist, x)

if result != -1:
    print('Found at index', result)
else:
    print('Not Found')
