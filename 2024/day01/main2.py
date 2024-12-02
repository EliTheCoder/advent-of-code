d = open("input.txt", "r").read()

lines = [[int(y) for y in x.split()] for x in d.splitlines()]

a, b = zip(*lines)

a, b = sorted(a), sorted(b)

similarity_scores = [b.count(x) * x for x in a]

print(sum(similarity_scores))





