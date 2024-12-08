inp = open("input.txt", "r").read().splitlines()

width = len(inp[0])
height = len(inp)

antennae = []

for y in range(height):
    for x in range(width):
        freq = inp[y][x]
        if freq != ".": antennae.append((x, y, freq))
    
antinodes = set()

def gen_antinode(a1, a2):
    x1, y1 = a1
    x2, y2 = a2
    if x1 < 0 or x1 >= width: return
    if y1 < 0 or y1 >= height: return
    if x2 < 0 or x2 >= width: return
    if y2 < 0 or y2 >= height: return
    antinodes.add((x2, y2))
    antinode = 2*x2 - x1, 2*y2 - y1
    gen_antinode((x2, y2), antinode)

for antenna1 in antennae:
    for antenna2 in antennae:
        if antenna1 is antenna2: continue
        a1x, a1y, a1f = antenna1
        a2x, a2y, a2f = antenna2
        if a1f != a2f: continue
        gen_antinode((a1x, a1y), (a2x, a2y))

print(len(antinodes))