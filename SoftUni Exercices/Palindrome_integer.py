while True:
    is_palindrome = False
    command = input()
    if command == 'END':
        break
    else:
        palindrom = 0
        nr = int(command)
        # if nr == nr[::-1]:
        #     is_palindrome = True
        while nr>0:
            rest = nr % 10
            palindrom = palindrom * 10 + rest
            nr = nr // 10
        if int(command) == palindrom:
            is_palindrome = True
        if is_palindrome == True:
            print('true')
        else:
            print('false')