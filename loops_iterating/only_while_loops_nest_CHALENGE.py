my_list = [[1, 3, 6, 11], [4, 2, 4], [9, 17, 16, 0],]
i = 0

while i < len(my_list):
    x = 0
    while x < len(my_list[i]):
        if my_list[i][x] % 2 == 0:
            print(my_list[i][x])
        x += 1
    i += 1      