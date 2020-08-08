a = int(input())
b = int(input())
c = int(input())


def add(first,second):
    summ = first + second
    return summ

s = add(a,b)
def subs(the_sum,third):
    f = the_sum- third
    return f
final = subs(s,c)

print(final)
