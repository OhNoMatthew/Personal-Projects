""" Simple Bubble Sort """

# 1. An array with values to sort
my_list: list = [64, 34 ,46, 79, 23, 54, 11, 6, 17]

n: int = len(my_list)

# 2. An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.
for i in range(n-1):
    
    # 3. An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)
