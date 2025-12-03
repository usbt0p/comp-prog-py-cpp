#https://aceptaelreto.com/problem/statement.php?id=540

n = int(input())

for _ in range(n):
    data = list(map(int, input().split(" ")))
    up = data[0] * data[1]
    down = data[2] * data[1] + data[3]
    updown = up + down
    
    print(down, updown) 