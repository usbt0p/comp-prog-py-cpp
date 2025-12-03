#https://adventofcode.com/2025/day/2

import sys

inp = sys.argv[1] #"adventOfCode2025/aoc3input1.txt" 
with open(inp, 'r', encoding='utf-8') as f:
    banks = f.read().split("\n")

banks = [[int(i) for i in list(b)] for b in banks]

# Part 1

def argmax(x):
    # get the index of the highest valued element
    return max(range(len(x)), key=lambda a : x[a])

def find_highers_joltage(banks):
    results = []
    for bank in banks:
        # find the bat with higest joltage
        max1 = argmax(bank)
        if max1 == len(bank) - 1: 
            # if its the last one, search next in the prev part
            max2 = argmax(bank[:max1])
            results.append(int(str(bank[max2]) + str(bank[max1])))
        else:
            # if we dont search from the last place, we have to do some
            # index manipulation to set the local index of b to be valid for bank
            b = bank[max1 + 1:]
            max2 = argmax(b) + max1 + 1
            results.append(int(str(bank[max1]) + str(bank[max2])))
        
    return results

res = find_highers_joltage(banks)
print("The higest joltages are:", res)
print("The sum is:", sum(res))



    
