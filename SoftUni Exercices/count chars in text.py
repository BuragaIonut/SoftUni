words = input().split()

data = {}

for word in words:
    for char in word:
        if char in data:
            data[char] += 1
        else:
            data[char] = 1
for key in data:
    print(f'{key} -> {data[key]}')