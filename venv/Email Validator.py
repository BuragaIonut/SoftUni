email = input()

while True:
    command = input().split()
    action = command[0]

    if action == 'Complete':
        break

    if action == 'Make':
        make_type = command[1]
        if make_type == 'Upper':
            email = email.upper()
            print(email)
        elif make_type == 'Lower':
            email = email.lower()
            print(email)

    elif action == 'GetDomain':
        count = int(command[1])
        print_value = email[(len(email)-count):]
        print(print_value)
    elif action == 'GetUsername':
        substring = ''
        has_reached_symbol = False
        for letter in email:
            if letter == '@':
                has_reached_symbol = True
                break
            substring += letter
        if has_reached_symbol:
            print(substring)
        else:
            print(f"The email {email} doesn't contain the @ symbol")

    elif action == 'Replace':
        char = command[1]
        email = email.replace(char, '-')
        print(email)

    elif action == 'Encrypt':
        [print(ord(l),end = ' ') for l in email]
        # print()
