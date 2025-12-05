ranges, _ = (x.splitlines() for x in open("./input.txt").read().split("\n\n"))

ranges = list(tuple(int(y) for y in x.split("-")) for x in ranges)
ranges = list((a,b+1) for a,b in ranges)

def reduce_range(a, b):
    aa, ab = a
    ba, bb = b
    if ba <= aa < bb: aa = bb
    if ba <= ab < bb: ab = ba
    if ab - aa <= 0: return None
    return aa, ab

ranges1 = []
for r1 in ranges:
    for r2 in ranges1:
        r1 = reduce_range(r1, r2)
        if r1 is None: break
    if r1 is not None:
        ranges1.append(r1)

ranges1.reverse()

ranges2 = []
for r1 in ranges1:
    for r2 in ranges2:
        r1 = reduce_range(r1, r2)
        if r1 is None: break
    if r1 is not None:
        ranges2.append(r1)

print(sum(b - a for a,b in ranges2))
