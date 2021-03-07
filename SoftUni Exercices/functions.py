a = int(input())
b = int(input())
c = int(input())
def smallest(a,b,c):
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    elif c < a and c < b:
        print(c)
smallest(a,b,c)