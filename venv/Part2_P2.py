import re

n = int(input())

for _ in range(n):
    barcode = input()
    pattern = r'@#+(?P<barcode>[a-zA-Z0-9]{5,}[A-Z])@#+'
    matches = re.match(pattern,barcode)
    if matches:
        second_pattern = r'[0-9]+'
        second_matches = re.findall(second_pattern,barcode)
        if len(second_matches) > 0:
            product_group = ''.join(second_matches)
            print(f'Product group: {product_group}')
        else:
            product_group = '00'
            print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
