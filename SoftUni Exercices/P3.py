items = list(input().split(', '))
while True:
    command = input()
    if command == 'Craft!':
        break
    else:
        command = list(command.split(' - '))
        if command[0] == 'Collect':
            if command[1] not in items:
                items.append(command[1])
        if command[0] == 'Drop' and command[1] in items:
            items.remove(command[1])
        if command[0] == 'Combine Items':
            combined = command[1].split(':')
            if combined[0] in items:
                index = items.index(combined[0])
                items.insert(index+1, combined[1])
        if command[0] == 'Renew':
            if command[1] in items:
                items.remove(command[1])
                items.append(command[1])
print(*items, sep =', ')