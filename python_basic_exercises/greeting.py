def greet(letter_code):
    dict_greetings = {'en': 'Hi!', 'fr':'Salut!', 'pt':'Ola!', 'de': 'Hallo!', 'sv':'Hej!', 'af':'Haal!'}
    if letter_code in dict_greetings:
        return dict_greetings[letter_code]
    else:
        return "Sorry, that wasn't in the registered name list!"

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
print(greet('askdf'))      #sorry, that wasn't in the registered name list!