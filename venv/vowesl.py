word  = input()

def vowels(word):
    contor = 0
    for i in word:
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "a" or i == "e" or i == "i" or i == "o" or i == "o":
            contor += 1
    print(contor)
vowels(word)
