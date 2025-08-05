"""Module providing a list of data types python version."""
# Will ask the day
# If it's friday it will make a new file and add the lyrics to friday night from yakuza

while True:
    print("Input a number from 1 - 7")
    user_input: int = input('What day is it today?: ')

    match user_input:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
            with open("FRIDAY_NIGHT.txt", 'w') as f:
                f.write("I'm ready to go tonight\nThere's a party, alright\nWe don't need the reason for joy, oh yeah\nTickin' down to midnight\nTonight's gonna be bright\nSo the groove will make me move, ooh, yeah\nI'm feeling like, I'm feeling just as fly\nCan't stop dancing all night long\nJumpin' up, shake it up, move your body\nDon't stop the music all night long\nKeep it on, it's friday night")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
            