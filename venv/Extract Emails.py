import re
text = input()

patern = "(\s[a-z0-9]+[_.-]?[a-z0-9]+@[a-z\-]+[.]{1}[a-z]+\.[a-z]+|\s[a-z0-9]+[_.-]?[a-z0-9]+@[a-z\-]+\.[a-z]+)"

emails = re.findall(patern, text)

[print (x) for x in emails]