usernames = input().split(', ')

def leng(word):
    if 3 <= len(word) <=16:
        return True

def contains(word):
    for letter in word:
        if (letter.isdigit() or letter.isalpha() or letter == '-' or letter == '_'):
            if letter != '@':
                is_ok = True
        else:
            is_ok = False
            break
    if is_ok:
        return True






for user in usernames:
    if leng(user) and contains(user):
        print(user)