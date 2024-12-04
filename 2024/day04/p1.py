d = open("input.txt", "r").read().splitlines()

width = len(d[0])
height = len(d)

xm = "XMAS"

kernel = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1),
]

def xmas(x, y, char, kn):
    if d[y][x] != xm[char]: return 0
    if char >= len(xm) - 1: return 1
    total = 0
    for i in range(len(kernel)) if kn is None else [kn]:
        kx, ky = kernel[i]
        cx, cy = x+kx, y+ky
        if cx < 0 or cx >= width: continue
        if cy < 0 or cy >= height: continue
        total += xmas(cx, cy, char+1, i)
    return total

count = 0

for j in range(height):
    for i in range(width):
        count += xmas(i, j, 0, None)

print(count)