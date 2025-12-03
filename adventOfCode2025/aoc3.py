#https://adventofcode.com/2025/day/2

import sys
import timeit

inp = sys.argv[1] #"aoc3input1.txt" 
with open(inp, 'r', encoding='utf-8') as f:
    banks = f.read().split("\n")

banks = [[int(i) for i in list(b)] for b in banks]

# Part 1

def argmax(x):
    # get the index of the highest valued element
    return max(range(len(x)), 
             # this is faster than lambda a : x[a]
            key=x.__getitem__)

def find_highest_joltages(banks):
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

# n = 100
# t = 0
# for _ in range(n):
#     t1 = timeit.default_timer()
#     res = find_highest_joltages(banks)
#     t2 = timeit.default_timer()
#     t += t2 - t1
# print(f"avg time over {n} runs:", t/n)

res = find_highest_joltages(banks)
print("The higest joltages are:", res)
print("The sum is:", sum(res))


# Parte 2

def argmin(x):
    return min(range(len(x)), key=x.__getitem__)

def find_highest_12_joltages(banks):
    results = []
    for bank in banks:
        # the initial number: start with the 12 last digits from the back
        init_num : list= bank[-12:]
        msd = init_num[0] # most significant digit
        
        for num in bank[:-12][::-1]: # for each number in (bank[:-12]) from the back to the front
            # search for a number higher or equal than the init_number's first digit
            if num >= msd:
                # if found, remove the init_number's first lowest 
                # digit and add to the front the newfound number
                # FIXME the problem is here! not the lowest one, but the most-significant lowest one with 
                lowest_n = min(init_num) 
                init_num.remove(lowest_n)
                init_num.insert(0, num)
                msd = num

        res = int("".join([str(i) for i in init_num]))
        results.append(res)
    return results

res = find_highest_12_joltages(banks)
print("The higest joltages are:", res)
print("The sum is:", sum(res))
#assert sum(res) == 3121910778619




    
