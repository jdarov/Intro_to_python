count = 0
scores = [96, 47, 113, 89, 100, 102]
count = sum(1 for score in scores if score >= 100)

print(count)