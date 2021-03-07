commands = int(input())
guests = []
for i in range(commands):
    line = input()
    data = line.split()
    if data[2] == 'going!':
        if data[0] not in guests:
            guests.append(data[0])
        else:
            print(f'{data[0]} is already in the list!')
    if data[2] == 'not':
        if data[0] not in guests:
            print(f'{data[0]} is not in the list!')
        else:
            guests.remove(data[0])
for i in guests:
    print(i)

