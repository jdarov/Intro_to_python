squares = [number*number for number in range(5)]
print(squares)

multiples_of_6 = [number for number in range(20) if number % 6 == 0]

print(multiples_of_6)

print(', '.join(map(str, multiples_of_6)))

even_squares = [number*number for number in range(10) if number % 2 == 0]

print(', '.join(map(str, even_squares)))