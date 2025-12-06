#https://adventofcode.com/2025/day/4
import sys


inp = f"aoc4input{sys.argv[1]}.txt"
with open(inp, 'r', encoding='utf-8') as f:
    map = [line.strip() for line in f.readlines()]

map = [[1 if j == "@" else 0 for j in i] for i in map]

# Part 1
# we add padding to do a sort of "convolution" without worrying about the indices
PAD = 1

def add_padding(map : list[list], padding):
    # first, side padding
    map = [[0]*padding + line + [0]*padding for line in map]

    # then add top an bottom padding
    top_p = [0]*len(map[0])
    map.insert(0, top_p)
    map.append(top_p)
    return map

m_h, m_w = len(map), len(map[0]) # keep the original size of the map

map = add_padding(map, PAD)

# now to index the eight adjacent squares and sum them
def kernel(h, w, map):
    ker = [ map[h-1][w-1], map[h-1][w], map[h-1][w+1],
            map[h][w-1],                map[h][w+1], # note the empty middle
            map[h+1][w-1], map[h+1][w], map[h+1][w+1]]
    return sum(ker)


def get_access_rolls(map, area):
    n_acc = 0       
    for idx in range(area):
        # get virtual indexes (where the coords would be if not for the padding)
        h, w = (idx//m_w)+PAD, (idx%m_h)+PAD 
        if map[h][w] == 1 and kernel(h, w, map) < 4:
            n_acc += 1 # then it's accessible

    return n_acc

print(get_access_rolls(map, m_w*m_h))


# part 2

def get_removed_rolls(map, area):
    remove_coords : list[tuple] = []      
    
    for idx in range(area):
        # get virtual indexes (where the coords would be if not for the padding)
        h, w = (idx//m_w)+PAD, (idx%m_h)+PAD 
        if map[h][w] == 1 and kernel(h, w, map) < 4:
            remove_coords.append((h, w))

    return remove_coords

# just for fun, dont use this with the big input lol
def printmap(map):
    for row in map:
        for col in row:
            if col: print("@", end="")
            else: print(".", end="")
        print()
    print()

total_removed = 0
while (coords := get_removed_rolls(map, m_h*m_w)):
    #printmap(map)
    for coord in coords:
        map[coord[0]][coord[1]] = 0
    total_removed += len(coords)

print(f"Removed a total of {total_removed} rolls")

        


     

