def factorial(num):
    counter = num

    while counter > 1:
        num *= (counter-1)
        counter -= 1
    return num

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(25))