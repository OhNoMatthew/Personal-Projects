
# def = Definition
def add(a: float, b:float) -> float:
    """Function printing python version."""
    print(f'Adding: {a} + {b}')
    return a + b

print(add(10,15))
print(add(15,45))

def greet(name: str, greeting: str = 'Hi') -> None:
    """Function printing python version."""
    print(f'{greeting}, {name}!')


greet('Bob', 'Ciao')


def func():
    """Function printing python version."""
    print('Hello')

func()