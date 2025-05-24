def starts_with(string, prefix):
    return True if prefix in string[0:len(prefix)] else False

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

print(starts_with('Hello', 'll'))     