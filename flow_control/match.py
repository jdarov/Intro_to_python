value = int(input('Input a value here to test the match/case: '))

match value:
    case 5 | 6 | 7:
        print('value is 5, 6, 7')
    case 8:
        print('value is also 8')
    case _:
        print('value is neither 5 or 6')

input1 = input('Now enter a sentence to practice Ternaries? ')

print('You need to type something!' if input1 == '' else input1)