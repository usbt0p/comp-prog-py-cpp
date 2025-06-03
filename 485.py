from sys import stdin

n_etapas = int(stdin.readline().strip())

while n_etapas != 0:

    out = []
    adder = 0
    etp = stdin.read(1)

    while etp != "\n":
        if etp != " ":
            adder += int(etp)
            out.append(adder)

        etp = stdin.read(1)

    print(out[::-1])

    n_etapas = int(stdin.readline().strip())

# TODO contraejemplos:

'''
1 2 3 4
[10, 6, 3, 1]
4
20 1 1 20
[6, 6, 4, 3, 2, 2]
'''