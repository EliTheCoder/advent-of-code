banks = [[int(y) for y in x.rstrip()] for x in open("./input.txt").readlines()]

def biggest(bank, count=11):
    if count <= 0: return max(bank)
    large = max(bank[:-count])
    large_index = bank.index(large)
    return large*10**count + biggest(bank[large_index+1:], count-1)

print(sum(biggest(bank) for bank in banks))
