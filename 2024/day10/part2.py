inp = open("input.txt", "r").read().splitlines()

width = len(inp[0])
height = len(inp)

data = [list(map(int, x)) for x in inp]

def move(x, y, d):
    match d:
        case 0: y -= 1
        case 1: x += 1
        case 2: y += 1
        case 3: x -= 1
    return x, y

def search(x, y, v):
    if x < 0 or x >= width: return 0
    if y < 0 or y >= height: return 0
    if data[y][x] != v: return 0
    if v == 9: return 1
    total = 0
    for i in range(4):
        cx, cy = move(x, y, i)
        total += search(cx, cy, v+1)
    return total

result = 0
for y in range(height):
    for x in range(width):
        if data[y][x] == 0:
            result += search(x, y, 0)

print(result)