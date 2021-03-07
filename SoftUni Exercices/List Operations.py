numbers = list(map(int, input().split()))
while True:
    line = input()
    if line == 'End':
        break
    data = line.split()
    if data[0] == 'Add':
        numbers.append(data[1])
    if data[0] == 'Insert':
        if int(data[2]) <= len(numbers) - 1:
            numbers.insert(int(data[2]), int(data[1]))
        else:
            print('Invalid index')
    if data[0] == 'Remove':
        if int(data[1]) <= len(numbers) - 1:
            numbers.pop(int(data[1]))
        else:
            print('Invalid index')
    if data[0] == 'Shift' and data[1] == 'left':
        for i in range(int(data[2])):
            numbers.append(numbers.pop(0))
    if data[0] == 'Shift' and data[1] == 'right':
        for i in range(int(data[2])):
            numbers.insert(0,numbers.pop(-1))

for i in numbers:
    print(i, end = ' ')
