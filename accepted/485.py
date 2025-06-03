#https://aceptaelreto.com/problem/statement.php?id=485

# golf that shit
while int(input()): print(*[sum(E[e:]) for e in range(len(E))]) if (E := [*map(int, input().split())]) else _


# Soluciçón legible:
'''
n_etapas = int(input())

while n_etapas != 0:

    etps = [int(i) for i in input().split()]

    print(*[sum(etps[e:]) for e in range(len(etps))])

    n_etapas = int(input())
'''