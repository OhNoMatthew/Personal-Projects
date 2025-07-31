import random

bot_name: str = "Bob"
print(f'Welcome to pick a number! I am {bot_name}, please type a difficulty')

# Set default value to False so each time you play it won't give a point

def easy(wins) -> int:
    while True:
        # Pick number from within the range
        random_number: int = random.randint(1,10)
        print("\nPick a number between 1 and 10")

        # Check if the input is a valid number within the range.
        try:
            user_guess = int (input("Enter your guess: ").strip())
            if not 1 <= user_guess <= 10:
                raise ValueError("The number is not within the range.")
        except ValueError:
            print("Bruh that's not a valid guess...")
            continue

        # Check if the number is the same as the bot. If you win you get a point added to wins.
        if user_guess == random_number:
            print("You guessed correct!")
            wins += 1

        # Not the same number
        else:
            print(f'Nice Try! The number was {random_number}')
        break
    return wins


def medium(wins) -> int:
    while True:
        # Pick number from within the range
        random_number: int = random.randint(1,30)
        print("\nPick a number between 1 and 30")

        # Check if the input is a valid number within the range.
        try:
            user_guess = int (input("Enter your guess: ").strip())
            if not 1 <= user_guess <= 30:
                raise ValueError("The number is not within the range.")
        except ValueError:
            print("Bruh that's not a valid guess...")
            continue

        # Check if the number is the same as the bot. If you win you get a point added to wins.
        if user_guess == random_number:
            print("You guessed correct!")
            wins += 1

        # Not the same number
        else:
            print(f'Nice Try! The number was {random_number}')
            break
    return wins

def hard(wins) -> int:
    while True:
        # Pick number from within the range
        random_number: int = random.randint(1,100)
        print("\nPick a number between 1 and 100")
        
       # Check if the input is a valid number within the range.
        try:
            user_guess = int (input("Enter your guess: ").strip())
            if not 1 <= user_guess <= 100:
                raise ValueError("The number is not within the range.")
        except ValueError:
            print("Bruh that's not a valid guess...")
            continue

        # Check if the number is the same as the bot. If you win you get a point added to wins.
        if user_guess == random_number:
            print("You guessed correct!")
            wins += 1

        # Not the same number
        else:
            print(f'Wrong! The number was {random_number}')
            break
    return wins
        
def impossible(wins) -> int:
    while True:
        # Pick number from within the range
        random_number: int = random.randint(1,10000000)
        print("\nPick a number between 1 and 10000000")
        user_guess: int = (input('Your guess: '))
        
        # Check if the input is a valid number within the range.
        try:
            user_guess = int (input("Enter your guess: ").strip())
            if not 1 <= user_guess <= 10000000:
                raise ValueError("The number is not within the range.")
        except ValueError:
            print("Bruh that's not a valid guess...")
            continue

        # Check if the number is the same as the bot. If you win you get a point added to wins.
        if user_guess == random_number:
            print("You guessed correct!")
            wins += 1

        # Not the same number
        else:
            print(f'DAMN you suck! The number was {random_number}')
            break
    return wins

def main() -> None:

    # Tally up wins. You start with zero wins
    wins: int = 0

    while True:
        user_input: str = input('\n*Easy* *Medium* *Hard* (Type win for score) > ').lower()

        # Choose Difficulty
        if user_input in ['easy']:
            print(f'You have chosen {user_input}')
            easy(wins)
            wins = easy(wins)
        elif user_input in ['medium']:
            print(f'You have chosen {user_input}')
            medium(wins)
            wins = medium(wins)
        elif user_input in ['hard']:
            print(f'You have chosen {user_input}')
            hard(wins)
            wins = hard(wins)
        elif user_input in ['impossible']:
            print(f'How did you find this mode? Well you asked for it... {user_input} mode.')
            impossible(wins)
            wins = impossible(wins)
        elif user_input in ['wins']:
            print(f'You have {wins} wins!')
        elif user_input in ['quit']:
            print('Program quit')
            break
        else:
            print('Please choose a valid difficulty')

main()
