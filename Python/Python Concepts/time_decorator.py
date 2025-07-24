"""Module providing a function printing python version."""

import time

def timer(func: str) -> None:
    """Function printing python version."""
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(str(end - start) + " seconds")

    return wrapper
