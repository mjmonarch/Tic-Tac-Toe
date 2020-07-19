# ---------------------------1---------------------------
# print("""X O X
# O X O
# X X O""")

# ---------------------------2---------------------------
# instructions = input()
# output = "---------\n"
# for i in range(0, 3):
#     output += f"| {instructions[i * 3]} {instructions[i * 3 + 1]} {instructions[i * 3 + 2]} |\n"
# output += "---------"
# print(output)

# # ---------------------------3---------------------------
# instructions = input("Enter cells: ")
#
#
# def draw_field(instructions_):
#     output = "---------\n"
#     for i in range(0, 3):
#         output += f"| {instructions[i * 3]} {instructions[i * 3 + 1]} {instructions[i * 3 + 2]} |\n"
#     output += "---------"
#     print(output)
#
#
# draw_field(instructions)
# field = [[instructions[i * 3], instructions[i * 3 + 1], instructions[i * 3 + 2]] for i in range(0, 3)]
# # print(field)
#
# xs = instructions.count('X')
# os = instructions.count('O')
# _s = instructions.count('_')
#
# while True:
#     if abs(xs - os) > 1:
#         print("Impossible")
#         break
#     xwin = False
#     ywin = False
#     if (field[0][0] == field[1][1] == field[2][2] == "X") or (field[2][0] == field[1][1] == field[0][2] == "X"):
#         xwin = True
#     if not xwin:
#         for i in range(0, 3):
#             if field[i][0] == field[i][1] == field[i][2] == "X":
#                 xwin = True
#                 break
#             if field[0][i] == field[1][i] == field[2][i] == "X":
#                 xwin = True
#                 break
#     if (field[0][0] == field[1][1] == field[2][2] == "O") or (field[2][0] == field[1][1] == field[0][2] == "O"):
#         ywin = True
#     if not ywin:
#         for i in range(0, 3):
#             if field[i][0] == field[i][1] == field[i][2] == "O":
#                 ywin = True
#                 break
#             if field[0][i] == field[1][i] == field[2][i] == "O":
#                 ywin = True
#                 break
#     if xwin and ywin:
#         print("Impossible")
#         break
#     if xwin:
#         print("X wins")
#         break
#     if ywin:
#         print("O wins")
#         break
#     if _s > 0:
#         print("Game not finished")
#     else:
#     break

# # ---------------------------4---------------------------
#
#
# def draw_field():
#     output = "---------\n"
#     for i in range(0, 3):
#         output += f"| {field[i][0]} {field[i][1]} {field[i][2]} |\n"
#     output += "---------"
#     print(output)
#
#
# global field
# instructions = input("Enter cells: ")
# instructions = instructions.replace('_', ' ')
# field = [[instructions[i * 3], instructions[i * 3 + 1], instructions[i * 3 + 2]] for i in range(0, 3)]
# draw_field()
# print(field)
#
# while True:
#     coordinates = input("Enter the coordinates: ").split()
#     for coordinate in coordinates:
#         if not coordinate.isnumeric():
#             print("You should enter numbers!")
#             break
#     else:
#         coordinates = [int(x) for x in coordinates]
#         for coordinate in coordinates:
#             if coordinate < 0 or coordinate > 3:
#                 print("Coordinates should be from 1 to 3!")
#                 break
#         else:
#             if field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
#                 print("This cell is occupied! Choose another one!")
#             else:
#                 break
#
# field[3 - coordinates[1]][coordinates[0] - 1] = 'X'
# print(field)
# draw_field()

# ---------------------------5---------------------------


def draw_field():
    output = "---------\n"
    for i in range(0, 3):
        output += f"| {field[i][0]} {field[i][1]} {field[i][2]} |\n"
    output += "---------"
    print(output)


def finished(x):
    result = [field[0][0] == field[1][1] == field[2][2] == x, field[2][0] == field[1][1] == field[0][2] == x]
    result.extend([field[j][0] == field[j][1] == field[j][2] == x for j in range(0, 3)])
    result.extend([field[0][j] == field[1][j] == field[2][j] == x for j in range(0, 3)])
    res = any(result)
    return any(result)


def check_input(coordinates):
    for coordinate in coordinates:
        if not coordinate.isnumeric():
            print("You should enter numbers!")
            return False
    coordinates = [int(x) for x in coordinates]
    for coordinate in coordinates:
        if coordinate < 0 or coordinate > 3:
            print("Coordinates should be from 1 to 3!")
            return False
    if field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def make_turn(x, coordinates):
    field[3 - int(coordinates[1])][int(coordinates[0]) - 1] = x


global field
# initializing field
field = [[' ' for x in range(3)] for y in range(3)]

# starting main cycle
for i in range(1, 10):
    move = 'X' if i % 2 else 'O'
    draw_field()
    while True:
        x_coordinates = input("Enter the coordinates: ").split()
        if check_input(x_coordinates):
            make_turn(move, x_coordinates)
            break
    if finished(move):
        draw_field()
        print(f"{move} wins")
        break
else:
    draw_field()
    print("Draw")
