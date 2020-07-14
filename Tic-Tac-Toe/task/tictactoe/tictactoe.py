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

# ---------------------------3---------------------------
instructions = input("Enter cells: ")


def draw_field(instructions_):
    output = "---------\n"
    for i in range(0, 3):
        output += f"| {instructions[i * 3]} {instructions[i * 3 + 1]} {instructions[i * 3 + 2]} |\n"
    output += "---------"
    print(output)


draw_field(instructions)
field = [[instructions[i * 3], instructions[i * 3 + 1], instructions[i * 3 + 2]] for i in range(0, 3)]
# print(field)

xs = instructions.count('X')
os = instructions.count('O')
_s = instructions.count('_')

while True:
    if abs(xs - os) > 1:
        print("Impossible")
        break
    xwin = False
    ywin = False
    if (field[0][0] == field[1][1] == field[2][2] == "X") or (field[2][0] == field[1][1] == field[0][2] == "X"):
        xwin = True
    if not xwin:
        for i in range(0, 3):
            if field[i][0] == field[i][1] == field[i][2] == "X":
                xwin = True
                break
            if field[0][i] == field[1][i] == field[2][i] == "X":
                xwin = True
                break
    if (field[0][0] == field[1][1] == field[2][2] == "O") or (field[2][0] == field[1][1] == field[0][2] == "O"):
        ywin = True
    if not ywin:
        for i in range(0, 3):
            if field[i][0] == field[i][1] == field[i][2] == "O":
                ywin = True
                break
            if field[0][i] == field[1][i] == field[2][i] == "O":
                ywin = True
                break
    if xwin and ywin:
        print("Impossible")
        break
    if xwin:
        print("X wins")
        break
    if ywin:
        print("O wins")
        break
    if _s > 0:
        print("Game not finished")
    else:
        print("Draw")
    break
