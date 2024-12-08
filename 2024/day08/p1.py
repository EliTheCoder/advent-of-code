inp = open("input.txt", "r").read().splitlines()

width = len(inp[0])
height = len(inp)

antennae = []

for y in range(height):
    for x in range(width):
        freq = inp[y][x]
        if freq != ".": antennae.append((x, y, freq))
    
antinodes = set()

for antenna1 in antennae:
    for antenna2 in antennae:
        if antenna1 is antenna2: continue
        a1x, a1y, a1f = antenna1
        a2x, a2y, a2f = antenna2
        if a1f != a2f: continue
        an1x, an1y = 2*a1x - a2x, 2*a1y - a2y
        an2x, an2y = 2*a2x - a1x, 2*a2y - a1y
        if an1x >= 0 and an1x < width and an1y >= 0 and an1y < height: antinodes.add((an1x, an1y))
        if an2x >= 0 and an2x < width and an2y >= 0 and an2y < height: antinodes.add((an2x, an2y))

print(len(antinodes))