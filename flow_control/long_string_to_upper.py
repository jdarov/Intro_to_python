def long_string_upper(string):
    if len(string) < 10:
        return string
    else:
        return string.upper()

user_input = input('Type a sentence more than 10 letters long: ')

print(long_string_upper(user_input))