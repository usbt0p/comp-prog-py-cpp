n = int(input())

for _ in range(n):
    n_cables = int(input())
    cables = input().split(" ")

    male_ct = 0
    female_ct = 0

    for c in cables:
        if c[0] == "M":
            male_ct += 1
        else:
            female_ct += 1
        if c[1] == "M":
            male_ct += 1
        else:
            female_ct += 1
    
    if male_ct == female_ct:
        print("POSIBLE")
    else:
        print("IMPOSIBLE")
        

