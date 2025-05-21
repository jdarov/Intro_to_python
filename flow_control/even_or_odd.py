number = int(input('Please enter a number: '))

def even_odd(num):
    if num%2 == 0:
        print(f'This number {num} is even!')
    else:
        print(f'This number {num} is an odd-ity HA! Its late...')

even_odd(number)