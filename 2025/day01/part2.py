val = 50
total = 0

for x in open("./input.txt").readlines():
    lr = -1 if x[0] == "L" else 1
    t = int(x.rstrip()[1:])
    if x[0] == "L" and val == 0: total -= 1
    val += t*lr
    c = -(val // 100)
    total += abs(c)
    val += c*100
    if x[0] == "L" and val == 0: total += 1
    print(x.rstrip(), c, val, total)

print(total)
