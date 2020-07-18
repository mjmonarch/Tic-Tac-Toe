words = input().split()
s_words = []
for word in words:
    if word.endswith('s'):
        s_words.append(word)
print("_".join(s_words))
