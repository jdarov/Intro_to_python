pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser') #since the value is a list, need the .append argument. = will replace the whole value 

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}