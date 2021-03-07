a = input()
b = input()

def chars_in_range(first, second):
    first_ascii = ord(first)
    second_ascii = ord(second)
    if first_ascii < second_ascii:
        for i in range(first_ascii + 1, second_ascii ):
            print(chr(i), end = ' ')
    else:
        for i in range(second_ascii + 1, first_ascii ):
            print(chr(i), end = ' ')
chars_in_range(a,b)