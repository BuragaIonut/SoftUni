is_item_obtained = False

materials = {}
trash = {}

materials['motes'] = 0
materials['shards'] = 0
materials['fragments'] = 0

while not is_item_obtained:
    command = input().split()

    for i in range(0, len(command),2):
        quantity = int(command[i])
        material = command[i+1].lower()

        if material == 'motes' or material == 'shards' or material == 'fragments':
            materials[material] += quantity
        else:
            if material not in trash:
                trash[material] = quantity
            else:
                trash[material] += quantity
        if materials['motes'] >= 250:
            materials['motes'] -+ 250
            print('Dragonwrath obtained!')
            is_item_obtained = True
            break
        elif materials['shards'] >= 250:
            materials['shards'] -+ 250
            print('Shadowmourne obtained!')
            is_item_obtained = True
            break
        elif materials['fragments'] >= 250:
            materials['fragments'] -+ 250
            print('Valanyr obtained!')
            is_item_obtained = True
            break
for (key,value) in sorted(materials.items(), key = lambda kvp: (-kvp[1], kvp[0])):
    print(f'{key}: {value}')

for (key,value) in sorted(trash.items(), key = lambda kvp: kvp[0]):
    print(f'{key}: {value}')