names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)

for i in names:
    upper_names.append(i.upper())
print(upper_names)   #will print the names upper twice but thats fine the end result of the solution is the same we would
                     # just have to delete the previous code!

