"""Module providing a list of data types python version."""
# Generators
# - Iterable -> can be looped over
# - Doesn't store all values
# - Generates value at demand

def count_up_to(n: int):
    """Function printing python version."""
    num = 1
    while num <= n:
        yield num
        num += 1

for number in count_up_to(5):
    print(number)
