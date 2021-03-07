passw = input()

def Is_Valid(password):
    valid_length = False
    two_digits = False
    only = True
    digit = 0
    let_dig = 0
    if len(password) >= 6 and len(password) <= 10:
        valid_length = True
    else:
        print('Password must be between 6 and 10 characters')
    for i in password:
        if  ((ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
            let_dig +=1
    if let_dig != len(password):
        only = False
    if not only:
        print('Password must consist only of letters and digits')
    for i in password:
        if ord(i) >= 48 and ord(i) <= 57:
            digit += 1
    if digit >= 2:
        two_digits = True
    else:
        print('Password must have at least 2 digits')
    if valid_length and two_digits and only:
        print('Password is valid.')
Is_Valid(passw)

