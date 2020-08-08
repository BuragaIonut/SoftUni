# Write your code here
text = input()
length = len(text)
i = 0
deleted = False
while i < length-1:
    if deleted:
        i -=1
        deleted = False
    if text[i+1] == text[i]:
        start = text[:i+1]
        end = text[i+2:]
        text = start + end
        length -= 1
        deleted = True
    i += 1
print(text)