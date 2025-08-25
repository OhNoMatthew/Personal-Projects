import random

def easy() -> None:
    # Pick number from within the range
    random_number = random.randint(1,10)
    print("I have my number...")

    # Check if the input is a valid number within the range.
    try:
        user_guess: int = int(input('Your guess: '))
    except not random.randint(1,10):
        print('Bruh that\'s not a valid guess...')
    
    # Check if the number is the same as the bot.
    if user_guess == random_number:
        print("You guessed correct!")

    # Not the same number
    else:
        print(f'Nice Try! The number was {random_number}')
