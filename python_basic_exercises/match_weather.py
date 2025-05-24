def weather(this_weather):
    match this_weather:
        case 'sunny':
            return "It's a beautiful day!"
        case 'rainy':
            return 'Grab your umbrella'
        case _:
            return "Let's stay inside."

print(weather('sunny'))
print(weather('rainy'))
print(weather('cloudy'))
print(weather(3))