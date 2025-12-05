inp = open("input.txt", "r").read().split()

data = [int(x) for x in inp]

def blink_stone(num):
    if num == 0: return [1]
    digits = str(num)
    num_digits = len(digits)
    if num_digits % 2 == 0: return [int(digits[:num_digits//2]), int(digits[num_digits//2:])]
    return [num*2024]

def transform(d):
    new_data = []
    for x in d:
        new_data += blink_stone(x)
    return new_data

for i in range(3):
    data = transform(data)
    print(len(data))
    print(data)

print(len(data))

