def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three    #this will print an error message as you did the function call without proper syntax (multiples_of_three())
