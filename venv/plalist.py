wagons = list(map(int, input().split()))
capcaity = int(input())

while True:
    line = input()
    if line == 'end':
        break
    data = line.split()
    if data[0] == 'Add':
        wagons.append(int(data[1]))
    else:
        passengers = int(line)

        for i in range(len(wagons)):
            if wagons[i] + passengers <= capcaity:
                wagons[i] += passengers
                break
for wagon in wagons:
    print(wagon, end = ' ')
