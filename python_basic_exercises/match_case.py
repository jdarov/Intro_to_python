animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh') #this is what it will print
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')