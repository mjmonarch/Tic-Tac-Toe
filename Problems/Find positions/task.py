# put your python code here
initial_list = input().split()
x = input()

if x not in initial_list:
    print("not found")
else:
    positions = []
    for i in range(len(initial_list)):
        if initial_list[i] == x:
            positions.append(i)
    positions.sort()
    positions = [str(x) for x in positions]
    print(" ".join(positions))
