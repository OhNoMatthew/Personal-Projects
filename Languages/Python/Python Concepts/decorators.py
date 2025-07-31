"""Module providing a list of data types python version."""
# Decorators
# - Cleaner
# - Reusable
# - Extra behaviour (without modifications)

def my_decorator(func: any) -> None:
    """Function printing python version."""
    def wrapper():
        print("Now Running " + func.__name__)
        func()

    return wrapper

@my_decorator
def say_hello():
    """Function printing python version."""
    print("Hello, World!")

say_hello()
