inp = open("input.txt", "r").read().splitlines()

width = len(inp[0])
height = len(inp)

mx, my = 0, 0
direction = 0

for y in range(height):
    for x in range(width):
        cell = inp[y][x]
        if cell == "^": mx, my = x, y

def infront():
    match direction:
        case 0: cx, cy = mx, my-1
        case 1: cx, cy = mx+1, my
        case 2: cx, cy = mx, my+1
        case 3: cx, cy = mx-1, my
    if cx < 0 or cx >= width: return "end"
    if cy < 0 or cy >= height: return "end"
    if inp[cy][cx] == "#": return "block"
    return "no"

crumbs = set()

while True:
    crumbs.add((mx, my))
    a = infront()
    match a:
        case "block":
            direction = (direction+1) % 4
        case "end": break
        case "no": 
            match direction:
                case 0: my -= 1
                case 1: mx += 1
                case 2: my += 1
                case 3: mx -= 1

print(len(crumbs))
        