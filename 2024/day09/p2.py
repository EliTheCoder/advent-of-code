inp = open("input.txt", "r").read()

def parse_disk(data):
    disk = []
    free = False
    i = 0
    for c in data:
        disk.append((int(c), -1 if free else i))
        if not free: i += 1
        free = not free
    return disk

def squash_disk(d):
    # d = [x for x in d if x[0] > 0]
    out = []
    for size, fid in d:
        if fid < 0 and out[-1][1] < 0:
            last = out.pop()
            out.append((last[0] + size, -1))
        elif size > 0:
            out.append((size, fid))
    if out[-1][1] < 0: out.pop()
    return out

def print_disk(d):
    out = ""
    for size, fid in d:
        out += ("." if fid < 0 else str(fid)) * size
    print(out)

def move_file(d, fi, fsize, fid):
    fit = next(((ind, (bsize, bid)) for (ind, (bsize, bid)) in enumerate(d) if bid < 0 and bsize >= fsize and ind < fi), None)
    if fit is None: return d
    ind, (bsize, bid) = fit
    d = [(x if x[1] != fid else (fsize, -1)) for x in d]
    d = d[:ind] + [(fsize, fid), (bsize-fsize, -1)] + d[ind+1:]
    d = squash_disk(d)
    return d

disk = parse_disk(inp)
disk = squash_disk(disk)

def defrag(d):
    highest = d[-1][1]
    for i in range(highest, -1, -1):
        fi, (fsize, fid) = next(x for x in enumerate(d) if x[1][1] == i)
        d = move_file(d, fi, fsize, fid)
    return d

def checksum(d):
    total = 0
    i = 0
    for size, fid in d:
        if fid >= 0:
            total += sum(range(i, i+size)) * fid
        i += size
    return total

print(checksum(defrag(disk)))


