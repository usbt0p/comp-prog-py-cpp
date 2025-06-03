n_etapas = int(input())

while n_etapas != 0:

    etps = [int(i) for i in input().split()]

    print(*[sum(etps[e:]) for e in range(len(etps))])

    n_etapas = int(input())