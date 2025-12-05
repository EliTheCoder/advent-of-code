inp = open("input.txt", "r").read().splitlines()

width = len(inp[0])
height = len(inp)

def xmas(x, y):
    if inp[y][x] != "A": return 0
    if x <= 0 or x >= width - 1: return 0
    if y <= 0 or y >= width - 1: return 0
    tl = inp[y - 1][x - 1]
    tr = inp[y - 1][x + 1]
    bl = inp[y + 1][x - 1]
    br = inp[y + 1][x + 1]
    for corner in [tl, tr, bl, br]:
        if corner not in "MS": return 0
    if tl == br: return 0
    if bl == tr: return 0
    return 1

count = 0

for j in range(height):
    for i in range(width):
        count += xmas(i, j)

print(count)