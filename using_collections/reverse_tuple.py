my_tuple = (1, 2, 3, 4, 5)
mutable_list = list(my_tuple)

my_tuple = tuple(mutable_list[-2:-len(my_tuple):-1])

print(f'The new tuple is {my_tuple}')