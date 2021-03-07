passw = input()

def is_Valid(password):
    digit = 0
    ony
    has_two_digits = False
    if len(password) >= 6 and len(password) <= 10:
        for i in password:
            if ord(i) >= 48 and ord(i) <= 57:
                digit += 1
            if digit >= 2:
                for i in password:
                    if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                        is_valid = True

                if is_valid is False:
                    print('Password must consist only of letters and digits')
        if digit < 2:
            print('Password must have at least 2 digits')
    else:
        print('Password must be between 6 and 10 characters')
    if is_valid == True:
        print('Password is valid.')
is_Valid(passw)

