forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short', 'Darovitz']

zipped_names = zip(forenames, surnames)
zipped_list = []

for forename, surname in zipped_names:
    print(f'{forename} {surname}')
    zipped_list.append(forename + ' ' + surname)

zipped_list.append(surnames[len(forenames)])


print(zipped_list)
#@print(', '.join(zipped_list))