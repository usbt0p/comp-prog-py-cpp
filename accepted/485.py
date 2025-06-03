#https://aceptaelreto.com/problem/statement.php?id=485

# golf that shit
while int(input()): print(*[sum(E[e:]) for e in range(len(E))]) if (E := [*map(int, input().split())]) else _


# Legible solution:
'''
We just have to calculate the total sum of 
the remaining (right hand side) stages from the current one, 
and add those to a list.
'''

'''
n_etapas = int(input())

while n_etapas != 0:

    etps = [int(i) for i in input().split()]

    print(*[sum(etps[e:]) for e in range(len(etps))])

    n_etapas = int(input())
'''