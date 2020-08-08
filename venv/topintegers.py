ar = list(map(int, input().split()))

for i in range(len(ar)):
    nr = ar[i]
    is_top = True
    for next_i in range (i +1, len(ar)):
        next_nr = ar[next_i]
        if nr <= next_nr:
            is_top = False
            break
    if is_top:
        print(nr, end = ' ')