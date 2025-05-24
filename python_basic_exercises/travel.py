destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city_name, destinations):
    end_of_list = 0
    while end_of_list < len(destinations):
        if destinations[end_of_list] == city_name:
            return True
        end_of_list += 1
    return False

print(contains('Barcelona', destinations))  #True
print(contains('Nashville', destinations))  #False