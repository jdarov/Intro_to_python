iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie', 'Ace')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)

print(list(zipped_iterables))

def merged_words(word1, word2):
    merged_words = []

    for a,b in zip(word1, word2):
        merged_words.append(a + b)

    merged_words.append(word1[len(word2):])
    merged_words.append(word2[len(word1):])

    return "".join(merged_words)

input1 = ''

while input1 != 'Cancel':
    input1 = input('Enter the first word (write Cancel to stop): ')
    input2 = input('Enter the second word: ')
    print(f'The two words with the letters mixed together is {merged_words(input1, input2)}')