numbers = list(map(int, input().split()))

while True:
    line = input()
    if line == 'end':
        break
    data = line.split()
    if data[0] == 'Delete':
        for i in numbers:
            if i == int(data[1]):
                numbers.remove(int(data[1]))
    if data[0] == 'Insert':
        numbers.insert(int(data[2]), int(data[1]))
for i in numbers:
    print(i, end = ' ')