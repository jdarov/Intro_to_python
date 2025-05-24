def weather(this_weather):
    return ("It's a beautiful day!" if this_weather == 'sunny'
            else 'Grab your umbrella' if this_weather == 'rainy'
            else "let's stay inside."
    )

print(weather('sunny'))
print(weather('rainy'))
print(weather('cloudy'))
print(weather(3))