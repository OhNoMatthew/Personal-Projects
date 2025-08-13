""" Improved Bubble Sort """

# Create array list
mylist: list = [7, 3, 9, 12, 11]

n: int = len(mylist)

# Outer Loop
for i in range (n-1):
    swapped: bool = False

    # Inner Loop
    for j in range (n-i-1):
        if mylist[j] > mylist[j+1]:
            
            # Swap places
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            swapped: bool = True
        if not swapped:
            break

print(mylist)
