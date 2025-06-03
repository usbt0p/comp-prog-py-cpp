#https://aceptaelreto.com/problem/statement.php?id=437

from sys import stdin

n_cases = int(stdin.readline()[:-1])

'''
Convert to seconds and then de-convert to datetime
with some integer arithmetic.
'''

for _ in range(n_cases):
    h, m, s = map(int, stdin.readline().strip().split(":"))
    total = h * 3600 + m * 60 + s
    start = 24*3600 - total
    
    sh = start // 3600
    sm = (start % 3600) // 60
    ss = start % 60
    print("{:02d}:{:02d}:{:02d}".format(sh, sm, ss))
    