n = int(input())

def NxN_matrix(number):
    for i in range(number):
        for j in range(number):
            print(f'{number} ', end = '')
        print()

NxN_matrix(n)