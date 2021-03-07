import re
total_cost = 0
names = []
prices = []
while True:
    line = input()
    if line == 'Purchase':
        break

    pattern = '>>(?P<Name>[a-zA-Z]+)<<(?P<Price>\d+\.*\d*)!(?P<Quantity>\d+)'
    results = re.finditer(pattern,line)
    for result in results:
        names.append(result.group("Name"))
        prices.append(result.group("Price"))
        total_cost += float(result.group("Price")) * float(result.group("Quantity"))
print('Bought furniture:')
for name in names:
    print(name)
print(f'Total money spent: {total_cost:.2f}')