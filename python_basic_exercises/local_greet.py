def local_greet(locale_code):
    def extract_language(local_code):
        return locale_code[0:2]

    def extract_region(locale_code):
        return locale_code[3:5]

    def greet(lang_code):
        greetings = {
            'en': different_english_greeting(),
            'fr': 'Salut!',
            'pt': 'Ola!',
            'de': 'Hallo!',
            'sv': 'Hej!',
            'af': 'Haal!'
        }
        return greetings.get(lang_code, "Sorry, that wasn't in the registered name list!")

    def different_english_greeting():
        region = extract_region(locale_code)
        return {
            'US': 'Hey!',
            'GB': 'Hello!',
        }.get(region, 'Howdy!')

    lang = extract_language(locale_code)
    return greet(lang)

print(local_greet('en_US.UTF-8'))  # Hey!
print(local_greet('en_GB.UTF-8'))  # Hello!
print(local_greet('en_AU.UTF-8'))  # Howdy!
print(local_greet('fr_FR.UTF-8'))  # Salut!
print(local_greet('fr_CA.UTF-8'))  # Salut!
print(local_greet('fr_MA.UTF-8'))  # Salut!
print(local_greet('no_tA.LOC-0'))  #Sorry that wasn't in the registered name list!
