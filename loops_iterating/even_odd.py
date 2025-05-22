my_list = [6, 3, 0, 11, 20, 4, 17]
another_list = [1, 3, 6, 11, 4, 2, 4, 9, 17, 16, 0]

index = 0

new_list = []

while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(f'This number is even {my_list[index]}')
    index += 1

for num in my_list:
    if num % 2 == 1:
        print(f'This number is odd {num}')


for num in another_list:
    if num % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')


print(new_list)