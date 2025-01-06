# https://aceptaelreto.com/problem/statement.php?id=100

'''
5
3524
1111
1121
6174
1893

'''


def recursive_kaprekar(k_in, n_iter):
    k = list(k_in)
    if len(set(k)) <= 1:
        return 8
    elif k_in == '6174':
        return n_iter

    if len(k) < 4:
        k.extend('0'*(4-len(k)))  # pad with 0's
    k.sort()
    k = ''.join(k)

    asc, desc = int(k), int(k[::-1])
    res = desc-asc
    print(desc, '-', asc, '=', res)

    return recursive_kaprekar(str(res), n_iter+1)


def iterative_kaprekar(k):
    res, n_iter = None, 0

    if len(set(k)) <= 1:
        return 8
    # elif k == '6174': return 0
    else:
        while res != 6174 and n_iter <= 7:
            asc, desc = int(k), int(k[::-1])
            res = desc-asc
            print(desc, '-', asc, '=', res)

            k = list(str(res))
            if len(k) < 4:
                k.extend('0'*(4-len(k)))  # pad with 0's
            k.sort()
            k = ''.join(k)
            n_iter += 1
        return n_iter


n_casos = int(input())
for _ in range(n_casos):

    k_in = input()
    k = list(k_in)
    if len(k) < 4:
        k.extend('0'*(4-len(k)))  # pad with 0's
    k.sort()
    k = ''.join(k)

    # result = recursive_kaprekar(k, 0)
    result = iterative_kaprekar(k)

    print(result)
