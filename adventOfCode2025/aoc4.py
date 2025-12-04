#https://adventofcode.com/2025/day/4
import sys

inp = sys.argv[1] 
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
    ker = [map[h-1][w-1], map[h-1][w], map[h-1][w+1],
                  map[h][w-1], 0, map[h][w+1], # note the 0 in the middle
                  map[h+1][w-1], map[h+1][w], map[h+1][w+1]]
    return sum(ker)

# get virtual indexes
idxs = [(i+PAD, j+PAD) for j in range(m_w) for i in range(m_h)]
n_acc = 0

for idx in idxs:
    h, w = idx
    if map[h][w] == 1 and kernel(h, w, map) < 4:
            n_acc += 1 # then it's accessible

print(n_acc)
