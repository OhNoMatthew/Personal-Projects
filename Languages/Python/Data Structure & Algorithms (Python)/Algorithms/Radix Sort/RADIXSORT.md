** Radix Sort **

Time Complexity:
Worst Case: O(n^2)
Average Case: O(nlog(n))
Best Case: O(n*k)

How it works:
1. Start with the least significant digit (rightmost digit).
2. Sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit in focus, and then put them back into array in the correct order.
3. Move to the next digit, and sort again, like in the step above, until there are no digits left.
