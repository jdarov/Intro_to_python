numbers = [1, 2, 3]
numbers2 = numbers

print(id(numbers) == id(numbers2))
print(numbers is numbers2)

print(id(numbers))
print(id(numbers2))

numbers2 = numbers.copy()

print(id(numbers))
print(id(numbers2))

print(numbers2 is numbers)