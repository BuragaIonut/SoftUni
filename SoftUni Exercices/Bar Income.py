import re
total_income = 0

while True:
    line = input()
    if line == 'end of shift':
        break
    # pattern1 = '%(?P<Name>[A-Z][a-z]+)%<(?P<Product>[a-zA-Z]+)>\|(?P<Count>\d+)\|(?P<Price>\d+\.\d+)\$'
    pattern = '%(?P<Name>[A-Z][a-z]+)%.*<(?P<Product>[a-zA-Z]+)>.*\|(?P<Count>\d+)\|[a-zA-Z]*(?P<Price>\d+\.*\d+)\$'
    results = re.finditer(pattern,line)
    for result in results:
        print(f'{result.group("Name")}: {result.group("Product")} - {float(result.group("Price"))*int(result.group("Count")):.2f}')
        total_income += float(result.group("Price"))*int(result.group("Count"))
print(f'Total income: {total_income:.2f}')
