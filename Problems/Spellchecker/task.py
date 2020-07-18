dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
incorrect_words = []
for word in words:
    if word not in dictionary:
        incorrect_words.append(word)
if not incorrect_words:
    print("OK")
else:
    print("\n".join(incorrect_words))
