cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if type(city) is str:
        print(len(city))
    continue