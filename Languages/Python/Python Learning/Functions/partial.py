"""Module providing a list of data types python version."""
from functools import partial

def specifications(colour: str, name: str, amount: int) -> None:
    """Function printing python version."""
    print(f'Specs: {colour=}, {name}, {amount=}.')

colour_and_name_specs: partial = partial(specifications, amount=10)
specify_amount: partial = partial (specifications, 'Blue', 'Bob')
specify_name: partial = partial (specifications, 'Orange', amount=20)

colour_and_name_specs('Red', 'Bob')
colour_and_name_specs('Blue', 'Kat')
colour_and_name_specs('Green', 'Bob')

specify_amount(500)

specify_name("Jon")
