digits = input()

odd_digits = [int(x) for x in digits if int(x) % 2 == 1]
print(odd_digits)