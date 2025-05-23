def all_actions():
    counter = 0
    def increment_counter():
        nonlocal counter                ### there is no defined global var counter, so we need to use nonlocal instead
        counter += 1
    print(counter)

    increment_counter()
    print(counter)

    increment_counter()
    print(counter)

    counter = 100
    increment_counter()
    print(counter)

all_actions()