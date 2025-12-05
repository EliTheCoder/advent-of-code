ranges, available = (x.splitlines() for x in open("./input.txt").read().split("\n\n"))

ranges = list(tuple(int(y) for y in x.split("-")) for x in ranges)
available = list(int(x) for x in available)

print(sum(1 for x in available if next((True for a,b in ranges if a <= x <= b), False)))

