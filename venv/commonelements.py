first = list(map(str, input().split()))
second = list(map(str, input().split()))
final = []
for i in range(len(second)):
    for j in range(len(first)):
        if second[i] == first[j]:
            final.append(second[i])

for i in final:
    print(i, end = ' ')
