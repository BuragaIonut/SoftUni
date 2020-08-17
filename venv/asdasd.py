import re
n = int(input())
for _ in range(n):
    barcode = input()
    pattern = "^@[#]+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$"
    matches = re.findall(pattern,barcode)
    if matches:
        pb = '(?P<prod>\d)'
        m = re.findall(pb,barcode)
        if m:
            print(f"Product group: {''.join(m)}")
        else:
            print(f"Product group: 00")
    else:
        print('Invalid barcode')