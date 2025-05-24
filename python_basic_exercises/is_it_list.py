def check_list(variable):
    if type(variable) is list:
        return True
    return False

some_value1 = [0,1,0,0,1]
some_value2 = 'I leave you my Kingdom, take good care of it'

print(check_list(some_value1))
print(check_list(some_value2))