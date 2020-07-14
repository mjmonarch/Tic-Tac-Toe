vowels = 'aeiou'

word = input()
word_vowels = [x for x in word if x in vowels]
print(word_vowels)