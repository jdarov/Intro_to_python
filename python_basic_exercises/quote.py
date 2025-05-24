def bruce_eckel_quote():
    print("Python is executable pseudocode")

bruce_eckel_quote()  #the return value is 'None' as the function only prints a statement but doesn't return a variable or value

print(type(bruce_eckel_quote()))   #will call function and print it's return type to check

def cite(author, quote):
    print(f'{author} said: {quote}')

cite('Bruce Eckel', 'Python is executable code')