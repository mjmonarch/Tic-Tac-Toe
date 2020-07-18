words = input().split()
words = [x.capitalize() if words.index(x) else x for x in words]
print("".join(words))
