dim = int(input())
triangle = [('#' * (2 * i + 1)).center((dim - 1) * 2 + 1) for i in range(dim)]
print("\n".join(triangle))
