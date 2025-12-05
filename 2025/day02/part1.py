data = [(int(y) for y in x.split("-")) for x in open("input.txt").read().split(",")]

def is_invalid(id: int) -> bool:
    s = str(id)
    h = len(s)//2
    return s[0:h] == s[h:]

total = 0

for start, end in data:
    for x in range(start, end+1):
        if is_invalid(x): total += x

print(total)
