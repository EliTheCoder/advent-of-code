inp = open("input.txt", "r").read().splitlines()

width = len(inp[0])
height = len(inp[0])

def move(x: int, y: int, d: int) -> tuple[int, int]:
    match d:
        case 0: y -= 1
        case 1: x += 1
        case 2: y += 1
        case 3: x -= 1
    return x, y

def reg(x: int, y: int, ch: str, counted: set[tuple[int, int]]) -> int:
    if inp[y][x] != ch: return 0
    if (x, y) in counted: return 0
    counted.add((x, y))
    total = 0
    for d in range(4):
        cx, cy = move(x, y, d)
        if cx < 0 or cx >= width:
            total += 1
            continue
        if cy < 0 or cy >= height:
            total += 1
            continue
        if inp[cy][cx] != ch: total += 1
        total += reg(cx, cy, ch, counted)
    return total

marked: set[tuple[int, int]] = set()

result = 0

for y in range(height):
    for x in range(width):
        if (x, y) in marked: continue
        counted: set[tuple[int, int]] = set()
        perim = reg(x, y, inp[y][x], counted)
        result += len(counted) * perim
        marked = marked.union(counted)

print(result)




