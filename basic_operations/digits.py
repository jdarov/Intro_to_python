number = 4936

ones = number % 10
number = number // 10
tens = number % 10
number = number // 10
hundreds = number % 10
number = number // 10

print (str(ones) + ' ' + str(tens) + ' ' + str(hundreds) + ' ' + str(number))