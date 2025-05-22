def check_for_3(my_list):
    for i in my_list:
        if int(i) == 3:
            return True
    return False
        
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']


print(f'The number appears in this list numbers: {check_for_3(numbers1)}')
print(f'The number appears in this list numbers: {check_for_3(numbers2)}')
print(f'The number appears in this list numbers: {check_for_3(numbers3)}')
#  print(f'The number appears in this list numbers: {check_for_3(numbers4)}')   # should return false because string! so function doesnt work

print(f'The number appears in this list numbers: {check_for_3(numbers5)}')

print(3 in numbers1)
print(3 in numbers4)
print(3 in numbers5)