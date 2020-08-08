first = int(input())
second = int(input())

def factorial(a,b):
    a_fact = 1
    b_fact = 1
    for i in range(1, a + 1):
        a_fact = a_fact * i
    for j in range(1,b + 1):
        b_fact = b_fact * j
    divide = a_fact / b_fact
    return  divide

dev = factorial(first, second)
print(f'{dev:.2f}')
