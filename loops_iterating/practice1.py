my_dict = {'a':1, 'b':2, 'c':3,}

my_list = []


for key, value in my_dict.items():
    tuple_pair = []
    tuple_pair.append(key)
    tuple_pair.append(value)
    
    my_list.append(tuple(tuple_pair))


print(my_list)