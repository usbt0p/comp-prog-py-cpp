import sys
import re

inp = sys.argv[1] #  "adventOfCode2025/aoc2input1.txt" 
with open(inp, 'r', encoding='utf-8') as f:
    moves = f.read().split(",")

moves = [tuple([int(n) for n in move.split("-")]) for move in moves]
print(moves)

# Part 1

def find_invalid_ids(ranges):
    """find the invalid IDs by looking for any ID which 
    is made *only* of some sequence of digits repeated *twice*
    """
    invalids = []

    for rg in ranges:
        for id in range(rg[0], rg[1]+1):
            # first, invalid ids must have an even number of digits
            sid = str(id)
            if len(sid) % 2 == 0:
                # then, since its only made of two repetitions, the 
                # repeats must be symetrical and can be split in the middle
                split = (len(sid) // 2)
                h1, h2 = int(sid[:split]), int(sid[split:])
                if h1 == h2:
                    invalids.append(id)

    return invalids

res = sum(find_invalid_ids(moves))
print("Sum of invalid ID's is:", res)

# Part 2

def find_really_invalid_ids(ranges):
    """an ID is invalid if it is made *only* of some 
    sequence of digits repeated *at least twice*
    """
    invalids = []

    for rg in ranges:
        for id in range(rg[0], rg[1]+1):
            sid = str(id)
            # loop trough the possible repetitions between min and max, where
            # min is the shortest (1) repetition possible
            # max is the greatest repetition possible (len(sid)//2+1)
            for seqlen in range(1, (len(sid) // 2) + 1 ):
                # and match each seqlen to the one that follows,
                # until it doesnt or until it ends
                seq = sid[:seqlen]
                match = re.search(f'({seq})+', sid).group()
                if len(match) == len(sid):
                    invalids.append(id)
                    break # break to match numbers like 222222 only once

    return invalids

res = sum(find_really_invalid_ids(moves))
print("Sum of the real invalid ID's is:", res)