def is_empty_or_blank(string):
    return string.isspace() or not string

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
print(is_empty_or_blank('------')) #False
print(is_empty_or_blank('                ')) #True