final_list = []

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

for i in zip(my_str, my_list, my_tuple, my_range):
    final_list.append(tuple(i))

print(final_list)