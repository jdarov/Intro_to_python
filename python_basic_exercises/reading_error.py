def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among([0, 0, 1, 0, 2, 0])     #typeError, one param = one arg, 6 given, need give 1 list arg
find_first_nonzero_among([1])                      #typeError, you can not iterate through an int object