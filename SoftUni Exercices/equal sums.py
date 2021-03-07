arr = list(map(int, input('nr').split()))
for i in range(len(arr)):
    s1 = 0
    s2 = 0
    for j in range(0, i):
        s1 = s1 + arr[j]
    for k in range(i+1, len(arr)):
        s2 = s2 + arr[k]
    
    if s1 == s2:
        print(i)