def dict_comp(a_set):
    new_dict = {name:len(name) for name in a_set if len(name) % 2 == 1}
    return new_dict

my_set = {'Fluffy', 'Butterscotch', 'Pudding', 'Cheddar', 'Cocoa',}
print(dict_comp(my_set))