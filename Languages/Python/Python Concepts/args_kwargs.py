"""Module providing a list of data types python version."""

def my_func(*args):
    print(args)

my_func(1, 2, "Hello, World")

def my_sum(num1, num2, *args):
    total = num1 + num2

    for number in args:
        total += number
    
    return total

print(my_sum(1, 1, 1))
print(my_sum(1, 2, 3, 4, 5))
print(my_sum(10, 20))

#kwargs = keyword args

def my_kwfunc(**kwargs):
    print(kwargs)

my_kwfunc(x=1, y=2, z=3)

# You can use both args and kwargs in one function
