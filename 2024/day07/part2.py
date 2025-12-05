inp = open("input.txt", "r").read().splitlines()

def parse(line):
    result, factors = line.split(": ")
    return int(result), [int(factor) for factor in factors.split()]

rows = [parse(line) for line in inp]

def calculate(result, factors):
    if len(factors) <= 1: return result == factors[0]
    if calculate(result, [factors[0] * factors[1]] + factors[2:]): return True
    if calculate(result, [factors[0] + factors[1]] + factors[2:]): return True
    if calculate(result, [int(str(factors[0]) + str(factors[1]))] + factors[2:]): return True
    return False

total = 0

for result, factors in rows:
    if calculate(result, factors): total += result

print(total)