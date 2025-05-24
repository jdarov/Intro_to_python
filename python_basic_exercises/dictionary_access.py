info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', 'uknown')) #this line is the problem, invoking .get allows you to set a default if the key/value pair is not there