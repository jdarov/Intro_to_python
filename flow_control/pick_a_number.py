def pick_a_number(value):
    if value > 0:
        if value <= 50:
            print(f'{value} is between 0 and 50')
        elif value <= 100:
            print(f'{value} is between 50 and 100')
        else:
            print(f'{value} is GREATER than 100 dummy!')
    else:
        print(f'{value} is less than 0')

user_input = int(input('Enter a number between -100 to 100: '))

pick_a_number(user_input)