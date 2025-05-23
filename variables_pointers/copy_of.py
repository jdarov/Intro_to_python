import copy

orig = [[1,2], 3, 4]

dup = copy.copy(orig)

print(orig is dup)      #False , two objects are made in seperate memory address at heap
print (orig == dup)      #True, all elements are the same in both lists
orig[2] = 44
print(dup)                # prints original list as it points to a different object than orig

print([orig[0] is dup[0]])     #True - they still point to the same nested list object
orig[0][1] = 22
print(dup[0])                   #[[1, 22]]