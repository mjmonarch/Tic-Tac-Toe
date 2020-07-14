n = int(input())

result_list = [name[0] for name in [input().split() for i in range(n)] if name[1] == 'win']
print(result_list, len(result_list), sep='\n')
