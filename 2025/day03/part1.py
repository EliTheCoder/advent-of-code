banks = [[int(y) for y in x.rstrip()] for x in open("./input.txt").readlines()]

def biggest(bank):
    large = max(bank[:-1])
    large_index = bank.index(large)
    small = max(bank[large_index+1:])
    return large*10+small

print(sum(biggest(bank) for bank in banks))
