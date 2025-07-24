"""Module providing a list of data types python version."""

double = lambda x: 2 * x

print(double(5))

pairs = [(1, 5), (2, 1), (3, 3)]

sorted_pairs = sorted(pairs, key=lambda x: x[1])

print (sorted_pairs)
