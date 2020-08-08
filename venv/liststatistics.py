n = int(input())
poz = []
neg = []
for i in range(n):
    m = int(input())
    if m >= 0:
        poz.append(m)
    else:
        neg.append(m)
count_poz = len(poz)
s = sum(neg)
print(f'Count of pozitives: {count_poz}')
print(f'Sum of negatives: {s}')

