inp = open("input.txt", "r").read().split()

class Stone():
    def __init__(self, num, mult=1):
        self.num = num
        self.mult = mult

    def __add__(self, other):
        assert self == other
        return Stone(self.num, self.mult+other.mult)
    
    def __eq__(self, other):
        return self.num == other.num
    
    def blink(self):
        if self.is_zero(): return [Stone(1, self.mult)]
        digits = str(self.num)
        num_digits = len(digits)
        if num_digits % 2 == 0: return [Stone(int(digits[:num_digits//2]), self.mult), Stone(int(digits[num_digits//2:]), self.mult)]
        return [Stone(self.num*2024, self.mult)]

data = [Stone(int(x)) for x in inp]

def transform(d):
    new_data = []
    for stone in d:
        new_stones = stone.blink()
        for new_stone in new_stones:
            dup = next((x for x in enumerate(new_data) if x[1] == new_stone), None)
            if dup is None: new_data.append(new_stone)
            else:
                i, old_stone = dup
                new_data[i] += new_stone
    return new_data

for i in range(75):
    data = transform(data)
    print(i)

print(sum(x.mult for x in data))

