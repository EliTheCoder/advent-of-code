inp = open("input.txt", "r").read()

def parse_disk(data):
    disk = []
    free = False
    i = 0
    for c in data:
        if free: disk += [None] * int(c)
        else:
            disk += [i] * int(c)
            i += 1
        free = not free
    return disk

disk = parse_disk(inp)

def defrag(d):
    while None in d:
        none = d.index(None)
        if none != len(d)-1: d[none] = d.pop()
        else: d.pop()
    return d

def checksum(d):
    return sum(i*n for i, n in enumerate(d))

print(checksum(defrag(disk)))


