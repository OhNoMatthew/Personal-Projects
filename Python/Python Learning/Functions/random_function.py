from random import choice, choices, sample

names: list[str] = ['Bob', 'George', 'Anna', 'Sophia']

winner: str = choice(names)
print(winner)

winners: list[str] = sample(names, k=2)
print(winners)

random_names: list[str] = choices(names, k=2)
print(random_names)
