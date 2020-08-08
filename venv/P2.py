health = 100
bitcoins = 0
rooms = list(input().split('|'))
index = 0
for room in rooms:
    index += 1
    room = list(room.split(' '))
    if room[0] == 'potion':
        heal = int(room[1])
        health += heal
        healed = heal
        if health > 100:
            rest = health - 100
            healed = heal - rest
            health = 100
        print(f'You healed for {healed} hp.')
        print(f'Current health: {health} hp.')
    elif room[0] == 'chest':
        print(f'You found {room[1]} bitcoins.')
        bitcoins += int(room[1])
    else:
        dmg = int(room[1])
        health -= dmg
        if health > 0:
            print(f'You slew {room[0]}.')
        else:
            print(f'You died! Killed by {room[0]}.')
            print(f'Best room: {index}')
            break

if health > 0:
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')