arr = list(map(int, input().split()))
contor = 1
endindex = 0
maxlen = 1
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        contor += 1
    else:
        contor = 1
    if contor > maxlen:
        maxlen = contor
        endindex = i+1

for i in range(endindex - maxlen + 1, endindex +1):
    print(arr[i], end = ' ')