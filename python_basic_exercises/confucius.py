def get_quote(person): #this will always return None, or NoneType
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.' #need return values to return a str from this func
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')