#https://aceptaelreto.com/problem/statement.php?id=114&potw=1

def last_num_factorial(n): 
    '''All factorials avobe 4! end in 0 because 
    they are multiples of 10 (n·...·5·...·2·1)'''
    match n:
        case 0: return 1
        case 1: return 1
        case 2: return 2
        case 3: return 6
        case 4: return 4
        case _: return 0

n_casos = int(input())

for _ in range(n_casos):
    print(last_num_factorial(int(input())))