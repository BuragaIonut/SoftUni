s = 0
input = input().split()
for nr in input:
    result = 0
    number = int(nr[1:-1])
    first_letter = nr[0]
    last_letter = nr[-1]
    if first_letter.isupper():
        letter = first_letter.upper()
        nr = ord(letter) - 64
        result = number/nr
        s += result
        result = 0
    elif first_letter.islower():
        first_letter = first_letter.upper()
        nr = ord(first_letter) - 64
        result = number * nr
        s += result
        result = 0
    if last_letter.isupper():
        letter = last_letter.upper()
        nr = ord(letter) - 64
        result = - nr
        s += result
        result = 0
    elif last_letter.islower():
        letter = last_letter.upper()
        nr = ord(letter) - 64
        result = nr
        s += result
        result = 0
print(f'{s:.2f}')