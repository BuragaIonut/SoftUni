arr = list(map(int, input().split()))
n = int(input())

for i in range(n, len(arr)):
    print(arr[i], end = ' ')
for i in range(n):
    print(arr[i], end = ' ')