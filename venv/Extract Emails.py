import re

text = input()

pattern = '[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]'

emails = re.findall(pattern, text)

for email in emails:
    print(email)
