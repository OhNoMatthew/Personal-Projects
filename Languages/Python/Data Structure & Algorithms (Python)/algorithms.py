""" Algorithms """

my_array = [ 8, 14, 9, 7, 11, 3]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value: ', minVal)
