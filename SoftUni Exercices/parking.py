n = int(input())

users = {}

for i in range(n):
    input_element = input().split()
    command = input_element[0]
    username = input_element[1]

    if command == 'register':
        license_nr = input_element[2]

        if username not in users:
            users[username] = license_nr
            print(f'{username} registered {license_nr} successfully')
        else:
            print(f'ERROR: already registered with plate numbert {license_nr}')
    else:
        if username not in users:
            print(f'ERROR: user {username} not found')
        else:
            users.pop(username)
            print(f'{username} unregistered successfully')
for username in users:
    print(f'{username} => {users[username]}')