** Counting Sort **

Time Complexity:
Worst Case: O(n^2)
Average Case: O(n + k)
Best Case: O(n)

How it works:
1. Create a new array for counting how many there are of the different values.
2. Go through the array that needs to be sorted.
3. For each value, count it by increasing the counting array at the corresponding index.
4. After counting the values, go through the counting array to create the sorted array.
5. For each count in the counting array, create the correct number of elements, with values that correspond to the counting array index.
