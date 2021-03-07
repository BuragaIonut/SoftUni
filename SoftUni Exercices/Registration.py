import re

n = int(input())

pattern = r'U\$(?P<username>[A-Z][a-z]{2,})U\$P@\$(?P<pass>[a-zA-Z]{5,}[0-9]+)P@\$'

counter = 0

for _ in range(n):
    email = input()
    matches = re.match(pattern,email)
    if matches:
        counter += 1
        user = matches.group('username')
        password = matches.group('pass')
        print('Registration was successful')
        print(f'Username: {user}, Password: {password}')
    else:
        print('Invalid username or password')

print(f'Successful registrations: {counter}')

