inp = open("input.txt", "r").read().splitlines()

width = len(inp[0])
height = len(inp)

mx, my = 0, 0
direction = 0

for y in range(height):
    for x in range(width):
        cell = inp[y][x]
        if cell == "^": mx, my = x, y

def move(pos, d):
    x, y = pos
    match d:
        case 0: y -= 1
        case 1: x += 1
        case 2: y += 1
        case 3: x -= 1
    return x, y

def infront(x, y, d):
    cx, cy = move((x, y), d)
    if cx < 0 or cx >= width: return "end"
    if cy < 0 or cy >= height: return "end"
    if inp[cy][cx] == "#" or inp[cy][cx] == "O": return "block"
    return "no"

def step(x, y, d):
    while True:
        a = infront(x, y, d)
        match a:
            case "block":
                d = (d+1) % 4
            case "end": return "end"
            case "no": 
                x, y = move((x, y), d)
                return x, y, d

blocks = set()

full_crumbs = set()

while True:
    full_crumbs.add((mx, my))
    a = infront(mx, my, direction)
    x, y, d = mx, my, direction
    s = step(x, y, d)
    if s == "end": break
    bx, by, _ = s
    inp[by] = inp[by][:bx] + "O" + inp[by][bx+1:]
    crumbs = set()
    result = None
    while True:
        if (x, y, d) in crumbs:
            result = "loop"
            break
        crumbs.add((x, y, d))
        s = step(x, y, d)
        if s == "end":
            result = "end"
            break
        x, y, d = s
    if result == "loop" and (bx, by) not in full_crumbs:
        blocks.add((bx, by))
    inp[by] = inp[by][:bx] + "." + inp[by][bx+1:]
    mx, my, direction = step(mx, my, direction)

for bx, by in blocks:
    inp[by] = inp[by][:bx] + "O" + inp[by][bx+1:]

print(len(blocks))
        