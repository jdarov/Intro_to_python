sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())   #this is a scope problem. we are mutating the list every time when we need to create a new list

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]