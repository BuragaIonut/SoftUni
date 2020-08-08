text = input()
strength = 0

i = 0
while i < len(text):
    symbol = text[i]
    if symbol == '>':
        strength += int(text[i + 1])
        i += 1
        continue
    if strength > 0:
        text = text[:i] + text[i+1:]
        i -=1
        strength -=1


    i +=1
print(text)