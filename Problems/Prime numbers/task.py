prime_numbers = [x for x in range(2, 1001) if all(x % y for y in range(2, x))]

# print(prime_numbers)
# print(5  % 1)
#
# for x in range(10):
#     print(str(x) + " " + str(all([x % y for y in range(2, x)])))
#     for y in range(2, x):
#         print(f"x={x}, y={y}: {x % y}")