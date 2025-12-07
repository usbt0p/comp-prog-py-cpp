#https://adventofcode.com/2025/day/5
import sys

inp = f"aoc5input{sys.argv[1]}.txt"
with open(inp, 'r', encoding='utf-8') as f:
    ranges, items = f.read().split("\n\n")
    ranges = [r.split("-") for r in ranges.split("\n")]
    ranges = [range(int(r[0]), int(r[1]) + 1) for r in ranges]
    items = list( map( int, items.split("\n")))

# naive solution
fresh_count = 0
for i in items:
    for r in ranges:
        if i in r:
            fresh_count += 1
            break

print(fresh_count)

