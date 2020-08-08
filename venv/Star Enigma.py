import re
messages = int(input())
attacked_planets = 0
destroyed_planets = 0
at_pl = []
d_pl = []

for i in range(messages):
    line = input()
    count = 0
    new_line = []
    for j in range(len(line)):
        if line[j] == 's' or line[j] == 't' or line[j] == 'a' or line[j] == 'r' or line[j] == 'S' or line[j] == 'T' or line[j] == 'A' or line[j] == 'R':
            count += 1
    for k in range(len(line)):
        letter = line[k]
        new_line.append(chr(ord(letter)-count))
    decriped = ''.join(new_line)
    pattern = '@(?P<Name>[A-Z][a-z]+).*:(?P<Population>\d+)!(?P<Attack>[A|D])!->(?P<Soldiers>\d+)'
    results = re.finditer(pattern,decriped)
    for result in results:
        if result.group('Attack') == 'A':
            attacked_planets += 1
            at_pl.append(result.group('Name'))
        if result.group('Attack') == 'D':
            destroyed_planets += 1
            d_pl.append(result.group('Name'))
print(f'Attacked planets: {attacked_planets}')
for plannet in at_pl:
    print(f'-> {plannet}')
print(f'Destroyed planets: {destroyed_planets}')
for plannet in reversed(d_pl):
    print(f'-> {plannet}')




