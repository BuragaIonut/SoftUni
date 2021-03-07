arr = list(map(int, input().split()))
n = int(input())
for i in range(len(arr)):
    one = arr[i]
    for j in range(i+1,len(arr)):
        two = arr[j]
        s = one + two
        if s == n:
            print(f'{one} {two}')