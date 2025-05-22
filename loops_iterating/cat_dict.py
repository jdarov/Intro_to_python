cats_colors = {'Tess': 'brown',
               'Leo': 'orange',
               'Fluffy': 'gray',
               'Ben': 'black',
               'Kat': 'orange',}

names = [(name.upper()+ ' is ' + color.upper()) for name,color in cats_colors.items() if name == 'Tess' or color == 'orange']

print(", ".join(names))
print(cats_colors.items())
print(names)