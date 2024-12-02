d = open("input.txt", "r").read()

lines = [[int(y) for y in x.split()] for x in d.splitlines()]

a, b = zip(*lines)

a, b = sorted(a), sorted(b)

pairs = zip(a, b)

dists = [abs(a - b) for a,b in pairs]

print(sum(dists))





