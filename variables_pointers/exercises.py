1. my_object1 == my_object2    #This checks the two objects, seperate or the same, for the elements
                               #are equal
                            
my_object1 is my_object2       #This will check if the two variables are pointing to the same object on the memory heap

2. set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)                     #42, Monty Python, (a, b, c), range(5, 10) 
                                #set2 points to same object as set1, and since sets are mutable, a mutation will be reflected in se

3. dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)               #creates pointer to a different object with dict() 
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])            #'The life of Brian' points to the first objects not the 2nd one created 

4. dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])       #[1, 42, 3] unless you use copy.deepcopy a shallow copy is made of the list, which means all objects list is pointing to reamin the same when assigning another variable

