raw_key = input()

while True:
    line = input().split('>>>')
    action = line[0]
    if action == 'Contains':
        substring = line[1]
        if substring in raw_key:
            print(f'{raw_key} contains {substring}')
        else:
            print('Substring not found!')

    elif action == 'Flip':
        how = line[1]
        start = int(line[2])
        end = int(line[3])
        if how == 'Upper' and start > 0 and end < len(raw_key):
            raw_key = raw_key.replace(raw_key[start:end],raw_key[start:end].upper())
            print(raw_key)
        elif how == 'Lower' and start > 0 and end < len(raw_key):
            raw_key = raw_key.replace(raw_key[start:end], raw_key[start:end].lower())
            print(raw_key)

    elif action == 'Slice':
        start = int(line[1])
        end = int(line[2])
        raw_key = raw_key[:start] + raw_key[end:]
        print(raw_key)
    elif action == 'Generate':
        print(f'Your activation key is: {raw_key}')
        break
