import re


def distance(kms):
    kms = int(kms)
    total_ran = 0
    while kms != 0:
        digit = kms%10
        total_ran += digit
        kms = kms // 10
    return total_ran


participants = input().split(', ')
partics = {}
while True:
    info = input()
    if info == 'end of race':
        break
    name_pattern = '(?P<Name>[a-zA-Z]+)'
    km_pattern = '(?P<Km>\d+)'
    name = ''.join(re.findall(name_pattern,info))
    kms = ''.join(re.findall(km_pattern,info))
    if name in participants:
        if name in partics.keys():
            partics[name] += distance(kms)
        else:
            partics[name] = distance(kms)
sorted = sorted(partics.items(), key=lambda item: item[1])
first_place = sorted[-1]
first_place_name = first_place[0]
print(f'1st place: {first_place_name}')
if len(sorted) >= 2:
    second_place = sorted[-2]
    second_place_name = second_place[0]
    print(f'2nd place: {second_place_name}')
if len(sorted) >= 3:
    third_place = sorted[-3]
    third_place_name = third_place[0]
    print(f'3rd place: {third_place_name}')








