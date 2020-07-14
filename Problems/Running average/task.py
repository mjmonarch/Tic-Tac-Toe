digits = input()
digits_list = [int(x) for x in digits]
digits_running_average = [(digits_list[x] + digits_list[x + 1]) / 2 for x in range(len(digits_list) - 1)]
print(digits_running_average)
