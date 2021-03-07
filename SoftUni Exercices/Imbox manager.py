users = {}

while True:
    line = input()
    if line == 'Statistics':
        break
    line = line.split('->')
    command = line[0]
    username = line[1]
    if command == 'Add':
        if username in users:
            print(f'{username} is already registered')
        else:
            users[username] = []
    elif command == 'Send':
        email = line[2]
        if username in users:
            users[username].append(email)
    elif command == 'Delete':
        if username in users:
            users.pop(username)
        else:
            print(f'{username} not found!')
length = len(users)
print(f'Users count: {length}')
for user in sorted(users.items(), key = lambda x: (-len(x[1]), x[0])):
    print(user[0])
    emails = user[1]
    for email in emails:
        print(f' - {email}')
