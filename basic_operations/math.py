balance = 1000000

compound_interest = 1000

INTEREST_RATE = 1.05

for i in range (5):
    compound_interest *= INTEREST_RATE

balance += compound_interest
print(int(compound_interest))
print(int(balance))
