val = 50
total = 0

for x in open("./input.txt").readlines():
    lr = -1 if x[0] == "L" else 1
    t = int(x.rstrip()[1:])
    val += t*lr
    val %= 100
    if val == 0: total += 1

print(total)
