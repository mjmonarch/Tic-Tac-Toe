digits = input()
digits_list = [int(x) for x in digits]
digits_running_total = [sum(digits_list[0:x + 1]) for x in range(len(digits_list))]
print(digits_running_total)
