grid = [line.rstrip() for line in open("./input.txt").readlines()]

width = len(grid[0])
height = len(grid)

def neighbors(pos):
    x, y = pos
    offsets = [
            (-1, -1),
            (-1,  0),
            (-1,  1),
            (0, -1),
            (0,  1),
            (1, -1),
            (1,  0),
            (1,  1),
            ]
    n = 0
    for ox, oy in offsets:
        nx, ny = x+ox, y+oy
        if nx < 0 or ny < 0: continue
        if nx >= width or ny >= height: continue
        if grid[ny][nx] == "@": n += 1
    return n

accessible = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] != "@": continue
        if neighbors((x, y)) < 4: accessible += 1


print(accessible)

