#https://adventofcode.com/2025/day/1
import sys

inp = "aoc1input2.txt" #sys.argv[1]
with open(inp, 'r', encoding='utf-8') as f:
    moves = f.read().split("\n")

# Part 1

def count_exact_zeroes(moves):
    start, c = 50, 0
    for move in moves:
        side, amount = move[0], int(move[1:])
        if side == "L":
            new = ((start - amount) + 100) % 100 # wrap around 99 to 0
        elif side == "R":
            new = ((start + amount) - 100) % 100
        start = new
        if new == 0: c += 1
    
    return c

print("The key is: ", count_exact_zeroes(moves))

# Part 2

def count_any_zeroes(moves):
    start, c = 50, 0
    
    for move in moves:
        side, amount = move[0], int(move[1:])

        if side == "L":
            new = ((start - amount) + 100) % 100 # wrap around 99 to 0
            # integer division counts the number of full circles
            div, mod = divmod(amount, 100)
            c += div
            # if the moving mod towards the left when not in 0 leaves us lower, it's a pass 
            if start - mod < 0 and start != 0: c += 1

        elif side == "R":
            new = ((start + amount) - 100) % 100
            
            div, mod = divmod(amount, 100)
            c += div
            # same logic as above but for the right
            if start + mod > 100 and start != 0: c += 1

        if new == 0: c += 1
        start = new
    
    return c

res = count_any_zeroes(moves)
print("The real key is: ", res)