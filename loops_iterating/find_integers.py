def find_integers(integers):
    new_list = [is_number for is_number in integers if type(is_number) is int]
    return new_list

my_tuple = (1, 'a', '1', 3, [7], 3.1415, -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)