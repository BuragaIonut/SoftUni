resources = []
dic = {}
while True:
    command = input()
    if command == 'stop':
        break
    resources.append(command)

for i in range(0,len(resources),2):
        key = resources[i]
        value = int(resources[i + 1])
        if key not in dic.keys():
            dic.update({key: value})
        else:
            dic[key] += int(value)
for kvp in dic.items():
    print(f'{kvp[0]} -> {kvp[1]}')