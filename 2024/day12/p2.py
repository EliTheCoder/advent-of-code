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

def matches(x: int, y: int, ch: str) -> bool:
    if x < 0 or x >= width: return False
    if y < 0 or y >= height: return False
    return inp[y][x] == ch

def check_corner(x: int, y: int, d: int) -> bool:
    ch = inp[y][x]
    cd = (d+1)%4
    cx, cy = move(x, y, cd)
    if not matches(cx, cy, ch): return True
    dx, dy = move(cx, cy, d)
    return matches(dx, dy, ch)

def reg(x: int, y: int, ch: str, counted: set[tuple[int, int]]) -> int:
    if not matches(x, y, ch): return 0
    if (x, y) in counted: return 0
    counted.add((x, y))
    total = 0
    for d in range(4):
        cx, cy = move(x, y, d)
        if not matches(cx, cy, ch):
            if check_corner(x, y, d):
                total += 1
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
        # print(inp[y][x], len(counted), perim)

print(result)




