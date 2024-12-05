from itertools import permutations

rules_input, updates_input = open("test.txt", "r").read().split("\n\n")

class Rule():
    def __init__(self, before, after):
        self.before = before
        self.after = after
    
    def matches(self, l):
        try:
            b = l.index(self.before)
            a = l.index(self.after)
        except ValueError:
            return True

        return b < a

    def match(self, bef, aft):
        if bef not in [self.before, self.after]: return True
        if aft not in [self.before, self.after]: return True
        if bef == self.before and aft == self.after: return True
        return False

rules = []

for rule in rules_input.splitlines():
    bef, aft = rule.split("|")
    rules.append(Rule(int(bef), int(aft)))


incorrects = []

for update in updates_input.splitlines():
    nums = [int(x) for x in update.split(",")]
    if any(not rule.matches(nums) for rule in rules):
        incorrects.append(nums)

def correction(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for rule in rules:
                if not rule.match(l[i], l[j]):
                    l[i], l[j] = l[j], l[i]
                    return correction(l)
    return l

total = 0


for incorrect in incorrects:
    incorrect = correction(incorrect)
    total += incorrect[len(incorrect)//2]

print(total)

