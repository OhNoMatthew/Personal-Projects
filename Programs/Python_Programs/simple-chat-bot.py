bot_name: str = 'Bob'
print(f'Hello! I\'m {bot_name}! How can I assist you today?')

while True:
    user_input: str = input('You: ').lower()

    if user_input in ['hi', 'hello']:
        print(f'{bot_name}: Hi there! How can I help you?')
    elif user_input in ['bye', 'see you']:
        print(f'{bot_name}: Goodbye! Have a great day!')
    elif user_input in ["+", 'add']:
        print(f'{bot_name}: Sure! Let\'s fo some addition! Please enter a valid number')
    try:
        num1: float = float(input('First number: '))
        num2: float = float(input('Second number: '))
        print(f'{bot_name}: The sum is {num1 + num2}')
    except ValueError:
        print(f'{bot_name}: Error, use valid numbers please!')
    else:
        print(f'{bot_name}: I\'m sorry, I don\'t understand that. Please try again.')
