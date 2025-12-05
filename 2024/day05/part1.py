rules_input, updates_input = open("input.txt", "r").read().split("\n\n")

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



rules = []

for rule in rules_input.splitlines():
    bef, aft = rule.split("|")
    rules.append(Rule(int(bef), int(aft)))

total = 0

for update in updates_input.splitlines():
    nums = [int(x) for x in update.split(",")]
    if all(rule.matches(nums) for rule in rules):
        total += nums[len(nums)//2]

print(total)

