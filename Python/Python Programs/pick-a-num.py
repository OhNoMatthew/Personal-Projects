import random

bot_name: str = "Jon"
print(f'Welcome to pick a number! I am {bot_name}, please type a difficulty')

def easy() -> None:
    while True:
        # Pick number from within the range
        random_number: int = random.randint(1,10)
        print("\nPick a number between 1 and 10")
        user_guess = int (input("Enter your guess: "))
        
        # Check if the nubmer is the same as the bot.
        if user_guess == random_number:
            print("You guessed correct!")
            break

        # Check if the input is a valid number within the range.
        try:
            if user_guess >= 10:
                raise ValueError("The number is not within the range.")
        except ValueError:
            print("Bruh that's not a valid guess...")

        # Not the same number
        else:
            print(f'Nice Try! The number was {random_number}')
            break

def medium() -> None:
    while True:
        # Pick number from within the range
        random_number: int = random.randint(1,30)
        print("\nPick a number between 1 and 30")
        user_guess = int (input("Enter your guess: "))
        
        # Check if the nubmer is the same as the bot.
        if user_guess == random_number:
            print("You guessed correct!")
            break

        # Check if the input is a valid number within the range.
        try:
            if user_guess >= 30:
                raise ValueError("The number is not within the range.")
        except ValueError:
            print("Bruh that's not a valid guess...")

        # Not the same number
        else:
            print(f'Nice Try! The number was {random_number}')
            break

def hard() -> None:
    while True:
        # Pick number from within the range
        random_number: int = random.randint(1,100)
        print("\nPick a number between 1 and 100")
        user_guess: int = int (input('Your guess: '))
        
        # Check if the nubmer is the same as the bot.
        if user_guess == random_number:
            print("You guessed correct! Now try the hidden mode impossible!")
            break

        # Check if the input is a valid number within the range.
        try:
            if user_guess >= 100:
                raise ValueError("The number is not within the range.")
        except ValueError:
            print("Bruh that's not a valid guess...")

        # Not the same number
        else:
            print(f'Wrong! The number was {random_number}')
            break
        
def impossible() -> None:
    while True:
        # Pick number from within the range
        random_number: int = random.randint(1,10000000)
        print("\nPick a number between 1 and 10000000")
        user_guess: int = (input('Your guess: '))
        
        # Check if the nubmer is the same as the bot.
        if user_guess == random_number:
            print("You guessed correct!")
            break

        # Check if the input is a valid number within the range.
        try:
            if user_guess >= 10000000:
                raise ValueError("The number is not within the range")
        except ValueError:
            print("Bruh that's not a valid guess...")

        # Not the same number
        else:
            print(f'DAMN you suck! The number was {random_number}')
            break

def main() -> None:
    while True:
        user_input: str = input('\n*Easy* *Medium* *Hard* > '.lower())
        wins: int = 0

        # Choose Difficulty
        if user_input in ['easy']:
            print(f'You have chosen {user_input}')
            easy()
        elif user_input in ['medium']:
            print(f'You have chosen {user_input}')
            medium()
        elif user_input in ['hard']:
            print(f'You have chosen {user_input}')
            hard()
        elif user_input in ['impossible']:
            print(f'How did you find this mode? Well you asked for it... {user_input} mode.')
            impossible()
        elif user_input in ['quit']:
            print('Program quit')
            break
        else:
            print('Please choose a valid difficulty')

main()
