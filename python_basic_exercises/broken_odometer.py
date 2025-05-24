car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

del car['mileage']
print(car['mileage'])   #gives a KEY ERROR because key and value no longer exist in dictionary