data = [(int(y) for y in x.split("-")) for x in open("input.txt").read().split(",")]

def is_invalid(id: int) -> bool:
    s = str(id)
    l = len(s)
    for i in range(1, l//2+1):
        if l % i != 0: continue
        if s == s[:i]*(l//i): return True
    return False

total = 0

for start, end in data:
    for x in range(start, end+1):
        if is_invalid(x): total += x

print(total)
