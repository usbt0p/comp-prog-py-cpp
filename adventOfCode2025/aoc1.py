#https://adventofcode.com/2025/day/1
import sys

with open(sys.argv[1], 'r', encoding='utf-8') as f:
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
            
            div, mod = divmod(start, 100)
            c += div

            if new > start: c+= 1

        elif side == "R":
            new = ((start + amount) - 100) % 100
            
            # integer division counts the number of full circles
            div, mod = divmod(start, 100)
            c += div
            # if the end is lower than the start another pass over 0
            if new < start: c += 1

        #if new == 0: c += 1
        start = new
    
    return c

print("The real key is: ", count_any_zeroes(moves))