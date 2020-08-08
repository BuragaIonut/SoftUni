n = int(input())

for i in range(16,n+1):
    sum_divisible = False
    holds = False
    help = i
    help2 = i
    summ = 0
    while help !=0:
        rest = help%10
        summ += rest
        help = help//10
    if summ%8 == 0:
        sum_divisible = True
    while help2 != 0:
        rest2 = help2%10
        if rest2 % 2 != 0:
            holds = True
        help2 = help2 //10
    if sum_divisible and holds:
        print(i)