word = input()

def middle_char(a_word):
    if len(a_word)%2 == 0:
        middle_indice = len(a_word)//2 -1
        next_middle_indice = middle_indice + 1
        middle = a_word[middle_indice:next_middle_indice+1]
        return middle
    else:
        middle_indice = len(a_word)//2
        middle = a_word[middle_indice]
        return middle
midchar = middle_char(word)
print(midchar)