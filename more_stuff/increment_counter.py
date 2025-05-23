counter = 0

def increment_counter():
    global counter
    counter += 1

print(counter)

increment_counter()
print(counter)

increment_counter()
print(counter)

counter = 100
increment_counter()
print(counter)