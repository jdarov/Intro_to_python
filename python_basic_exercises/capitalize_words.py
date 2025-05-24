string = 'launch school tech & talk'

list_of_string = string.split()
final_string = []
for words in list_of_string:
    final_string.append(words[0].upper() + words[1:])

print(' '.join(final_string))