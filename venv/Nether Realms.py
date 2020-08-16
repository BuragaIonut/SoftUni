import re
line = re.split('\\s*,\\s*', input())
lista = {}
for nume in line:
    sh = 0
    sd = 0
    matchesh = ''.join(re.findall('[^\\d+*/\\\.-]', nume))

    for x in matchesh:
        sh += ord(x)

    pattern = '\\d+\\.\\d+|-\\d+\\.\\d+|\\d+\\.\\d+|\\d+|-\\d+|\\d+'
    matchesd = re.findall(pattern, nume)
    for x in matchesd:
        sd += float(x)

    listaop = re.findall('[*/]' , nume)
    for x in listaop:
        if x == "*":
            sd *= 2
        elif x == "/":
            sd /= 2
    lista[nume] = [sh, sd]
lista = dict(sorted(lista.items(), key = lambda x: x[0]))
for (k,v) in lista.items():
    print(f"{k} - {v[0]} health, {'{:.2f}'.format(v[1])} damage")
